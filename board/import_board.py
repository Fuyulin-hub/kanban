"""Import the reviewed CSV through gh only; standard-library Python 3, no token handling."""
import argparse
import csv
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from collections import Counter

HERE = Path(__file__).resolve().parent
TITLE = 'Group Task Board'
MANAGED = {'source:wechat', 'needs-review', 'status:completed', 'status:unfinished', 'status:in-progress'}
FILES = ('issues.csv', 'setup.sh', 'import_board.py', 'manifest.md', 'audit.md')
TABLE_START = '<!-- TASK_TABLE_START -->'
TABLE_END = '<!-- TASK_TABLE_END -->'


def load_rows(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ['title', 'body', 'labels', 'status_column']:
            raise ValueError('CSV columns must be exactly title,body,labels,status_column')
        rows = list(reader)
    seen = set()
    for row in rows:
        if not row['title'].startswith('[WeChat] ') or row['title'] in seen:
            raise ValueError('Invalid title prefix or duplicate CSV title')
        seen.add(row['title'])
        labels = set(filter(None, row['labels'].split(',')))
        if not labels <= MANAGED or 'source:wechat' not in labels:
            raise ValueError('Unknown label or missing source label')
        if sum(x.startswith('status:') for x in labels) != 1:
            raise ValueError('Each task must have exactly one status label')
        if row['status_column'] not in {'Todo', 'In Progress', 'Done', 'Needs Review'}:
            raise ValueError('Unknown board column')
        if ('needs-review' in labels) != (row['status_column'] == 'Needs Review'):
            raise ValueError('Needs Review column and needs-review label disagree')
        if 'Recorded owner\n\nUnassigned\n' in row['body'] and 'needs-review' not in labels:
            raise ValueError('Unassigned tasks must be flagged for review')
        for heading in ('Recorded owner', 'Status', 'Evidence', 'Source files', 'Confidence', 'Review reason'):
            if f'## {heading}\n' not in row['body']:
                raise ValueError('Incomplete issue body structure')
        if re.search(r'(?<!\d)1[3-9]\d{9}(?!\d)', row['body']):
            raise ValueError('Possible unredacted phone number detected')
        if not re.search(r'<!-- wechat-task:T\d+ -->', row['body']):
            raise ValueError('Missing stable task ID')
    return rows


def choose(existing, title):
    hits = [x for x in existing if x.get('title') == title and not x.get('pull_request')]
    if len(hits) > 1:
        raise RuntimeError(f'Multiple issues share this title; resolve duplicates manually: {title}')
    return hits[0] if hits else None


def label_set(issue):
    return {x['name'] if isinstance(x, dict) else x for x in issue.get('labels', [])}


def normalize_body(body):
    return (body or '').replace('\r\n', '\n').rstrip('\n')


def merge_execution_plan(generated, old_body):
    """Keep the separately reviewed plan when reimporting original chat evidence."""
    start = '<!-- execution-plan:start -->'
    end = '<!-- execution-plan:end -->'
    if start in generated:
        return generated
    old_body = old_body or ''
    if start not in old_body and end not in old_body:
        return generated
    if old_body.count(start) != 1 or old_body.count(end) != 1:
        raise ValueError('Missing or duplicate plan markers; stopped to preserve reviewed content')
    begin = old_body.index(start)
    if old_body.index(end) < begin:
        raise ValueError('Invalid execution-plan marker order')
    return generated.rstrip() + '\n\n' + old_body[begin:]


def desired_labels(old, row):
    return (label_set(old) - MANAGED) | set(row['labels'].split(','))


def is_confirmed(issue, titles):
    return (issue['title'] in titles or
            bool(label_set(issue) & {'manual-confirmed', 'manual-confirmed'}) or
            '<!-- manual-confirmed -->' in (issue.get('body') or ''))


def needs_move(item, wanted):
    return (item or {}).get('status', '').casefold() != wanted.casefold()


class Runner:
    def __init__(self, log):
        self.log = log

    def run(self, *args, cwd=None, json_result=False, allowed_failure=False):
        command = [str(x) for x in args]
        env = os.environ.copy()
        env['GH_PROMPT_DISABLED'] = '1'
        env['GH_PAGER'] = 'cat'
        env['GIT_TERMINAL_PROMPT'] = '0'
        p = subprocess.run(command, cwd=cwd, env=env, capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
        self.log.append(f'- `{shlex.join(command)}` → exit {p.returncode}')
        if p.returncode:
            safe = re.sub(r'gh[pousr]_[A-Za-z0-9_]+', '[TOKEN REDACTED]', p.stderr.strip())
            self.log.append('  - Error: ' + safe[:1600].replace('\n', ' / '))
            if not allowed_failure:
                raise RuntimeError(safe or f'Command failed: {command[0]}')
            return None
        if json_result:
            value = json.loads(p.stdout)
            summary = f'JSON {type(value).__name__}'
            if isinstance(value, list):
                summary += f', {len(value)}top-level records'
            elif isinstance(value, dict):
                summary += '; fields ' + ', '.join(value.keys())[:250]
                if value.get('errors'):
                    self.log.append('  - GraphQL errors: ' + json.dumps(value['errors'], ensure_ascii=False)[:1000])
                    if allowed_failure:
                        return None
                    raise RuntimeError('GraphQL returned errors; stopped')
            self.log.append('  - ' + summary + '; unrelated repository content is omitted from the audit.')
            return value
        self.log.append('  - ' + (p.stdout.strip()[:350].replace('\n', ' / ') or 'Succeeded; no stdout'))
        return p.stdout.strip()

    def gh(self, *args, **kwargs):
        return self.run('gh', *args, **kwargs)

    def graphql(self, query, variables, allowed_failure=False):
        # Structured JSON avoids shell quoting and permits arrays without interpolating chat text.
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', suffix='.json', delete=False) as f:
            json.dump({'query': query, 'variables': variables}, f, ensure_ascii=False)
            path = Path(f.name)
        try:
            return self.gh('api', 'graphql', '--input', str(path), json_result=True,
                           allowed_failure=allowed_failure)
        finally:
            path.unlink(missing_ok=True)


def flatten_pages(result):
    return [x for page in result for x in page]


def query_views(run, project_id):
    nodes = []
    after = None
    while True:
        data = run.graphql('''query($id:ID!,$after:String){node(id:$id){... on ProjectV2{
          views(first:100,after:$after){nodes{id name layout} pageInfo{hasNextPage endCursor}}}}}''',
                           {'id': project_id, 'after': after})
        connection = data['data']['node']['views']
        nodes.extend(connection['nodes'])
        if not connection['pageInfo']['hasNextPage']:
            return nodes
        after = connection['pageInfo']['endCursor']


def ensure_board_view(run, project_id):
    views = query_views(run, project_id)
    if any(x['layout'] == 'BOARD_LAYOUT' for x in views):
        return
    run.graphql('''mutation($input:CreateProjectV2ViewInput!){createProjectV2View(input:$input){
      projectV2View{id name layout}}}''', {'input': {'projectId': project_id, 'name': TITLE, 'layout': 'BOARD_LAYOUT'}})
    if not any(x['layout'] == 'BOARD_LAYOUT' for x in query_views(run, project_id)):
        raise RuntimeError('No native board view verified; completion cannot be claimed')


def status_field(run, number, owner):
    result = run.gh('project', 'field-list', number, '--owner', owner,
                    '--limit', '1000', '--format', 'json', json_result=True)
    fields = [f for f in result['fields'] if f.get('name') == 'Status']
    if len(fields) != 1 or 'options' not in fields[0]:
        raise RuntimeError('A unique single-select Status field is required')
    return fields[0]


def ensure_review_option(run, field, log):
    if any(x['name'] == 'Needs Review' for x in field['options']):
        return True
    schema = run.graphql('query{__type(name:"ProjectV2SingleSelectFieldOptionInput"){inputFields{name}}}', {}, True)
    if not schema or 'id' not in {x['name'] for x in schema['data']['__type']['inputFields']}:
        log.append('- Review-column fallback: cannot guarantee option ID preservation; use needs-review + Todo.')
        return False
    info = run.graphql('''query($id:ID!){node(id:$id){... on ProjectV2SingleSelectField{
      id options{id name color description}}}}''', {'id': field['id']}, True)
    if not info:
        log.append('- Review-column fallback: cannot read all options; use needs-review + Todo.')
        return False
    options = info['data']['node']['options']
    # Existing IDs are essential: omitting them can clear existing project item values.
    new = options + [{'name': 'Needs Review', 'color': 'ORANGE', 'description': 'Ownership, status or scope requires human confirmation'}]
    result = run.graphql('''mutation($input:UpdateProjectV2FieldInput!){updateProjectV2Field(input:$input){
      projectV2Field{... on ProjectV2SingleSelectField{id options{id name}}}}}''',
                         {'input': {'fieldId': field['id'], 'singleSelectOptions': new}}, True)
    if not result:
        log.append('- Review-column fallback: GraphQL cannot add the option; use needs-review + Todo.')
        return False
    return True


def replace_table(manifest, records):
    lines = ['| ID | Task | Issue | Source status | Column | Recorded owner |',
             '| --- | --- | --- | --- | --- | --- |']
    for record in records:
        safe = lambda value: str(value).replace('|', '\\|').replace('\n', ' ')
        lines.append('| ' + ' | '.join(safe(record[x]) for x in ('id', 'title', 'issue', 'status', 'column', 'owner')) + ' |')
    return manifest.split(TABLE_START)[0] + TABLE_START + '\n' + '\n'.join(lines) + '\n' + TABLE_END + manifest.split(TABLE_END)[1]


def main(argv=None):
    parser = argparse.ArgumentParser(description='Import a redacted task CSV to a native GitHub board and open a PR for board files only')
    parser.add_argument('--repo', default='Fuyulin-hub/kanban')
    parser.add_argument('--validate-only', action='store_true', help='Validate the local CSV without calling gh or git')
    args = parser.parse_args(argv)
    rows = load_rows(HERE / 'issues.csv')
    if args.validate_only:
        print(json.dumps({'tasks': len(rows), 'columns': dict(Counter(r['status_column'] for r in rows)),
                          'validation': 'PASS', 'external_writes': 0}, ensure_ascii=False, indent=2))
        return 0
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', args.repo):
        raise ValueError('--repo must have the form owner/repo')
    log = ['\n## Authenticated-machine execution log', '', f'UTC start time {dt.datetime.now(dt.timezone.utc).isoformat()}']
    run = Runner(log)
    clone = None
    try:
        # Required sequence. Any failure here stops immediately; no alternate connector/API is used.
        if not shutil.which('gh'):
            raise RuntimeError('gh not found; install GitHub CLI, sign in and grant project access.')
        run.gh('--version')
        run.gh('auth', 'status')
        run.gh('project', 'list', '--limit', '1')
        repo = run.gh('repo', 'view', args.repo, '--json', 'nameWithOwner,owner,defaultBranchRef', json_result=True)
        account = run.gh('api', 'user', '--jq', '.login')
        account_id = run.gh('api', 'user', '--jq', '.id')
        owner = repo['owner']['login']
        repository = repo['nameWithOwner']
        if not (repo.get('defaultBranchRef') or {}).get('name'):
            raise RuntimeError('The target repository is empty. Initialize its default branch with a README first; this script does not initialize or push directly to main.')
        base = repo['defaultBranchRef']['name']
        if not shutil.which('git'):
            raise RuntimeError('git is unavailable; cannot publish a PR.')
        existing = flatten_pages(run.gh('api', '--paginate', '--slurp',
                                        f'repos/{repository}/issues?state=all&per_page=100', json_result=True))
        for row in rows:
            choose(existing, row['title'])
        # A clean temporary clone isolates the import from existing working files.
        clone = Path(tempfile.mkdtemp(prefix='wechat-board-')) / 'repo'
        run.gh('repo', 'clone', repository, str(clone), '--', '--branch', base)
        run.run('git', 'config', 'user.name', account, cwd=clone)
        run.run('git', 'config', 'user.email', f'{account_id}+{account}@users.noreply.github.com', cwd=clone)
        branch = 'board/wechat-' + dt.datetime.now(dt.timezone.utc).strftime('%Y%m%d-%H%M%S')
        run.run('git', 'switch', '-c', branch, cwd=clone)
        prior = clone / 'board/manifest.md'
        confirmed = []
        if prior.exists():
            match = re.search(r'<!-- confirmed-titles: (.*?) -->', prior.read_text(encoding='utf-8'), re.S)
            if match:
                confirmed = json.loads(match.group(1))
        target = clone / 'board'
        target.mkdir(exist_ok=True)
        for name in FILES:
            shutil.copyfile(HERE / name, target / name)
        projects = run.gh('project', 'list', '--owner', owner, '--limit', '10000', '--format', 'json', json_result=True)
        if projects.get('totalCount', 0) > len(projects['projects']):
            raise RuntimeError('Project list truncated; stopped to avoid duplicates.')
        hits = [p for p in projects['projects'] if p['title'] == TITLE]
        if len(hits) > 1:
            raise RuntimeError('Multiple projects share the title; select or deduplicate them manually.')
        project = hits[0] if hits else run.gh('project', 'create', '--owner', owner, '--title', TITLE,
                                            '--format', 'json', json_result=True)
        number = str(project['number'])
        project = run.gh('project', 'view', number, '--owner', owner, '--format', 'json', json_result=True)
        ensure_board_view(run, project['id'])
        field = status_field(run, number, owner)
        review_available = ensure_review_option(run, field, log)
        field = status_field(run, number, owner)
        options = {x['name'].casefold(): x['id'] for x in field['options']}
        for status in ('Todo', 'In Progress', 'Done'):
            if status.casefold() not in options:
                raise RuntimeError('Status lacks a required option: ' + status)
        if review_available and 'needs review' not in options:
            raise RuntimeError('The review option failed read-back verification.')
        labels = flatten_pages(run.gh('api', '--paginate', '--slurp', f'repos/{repository}/labels?per_page=100', json_result=True))
        known_labels = {x['name'] for x in labels}
        for name in sorted(MANAGED - known_labels):
            run.gh('label', 'create', name, '--repo', repository,
                   '--color', 'd4c5f9' if name == 'needs-review' else 'd9eaf7')
        listed = run.gh('project', 'item-list', number, '--owner', owner, '--limit', '10000',
                        '--format', 'json', json_result=True)
        if listed.get('totalCount', 0) > len(listed['items']):
            raise RuntimeError('Project item list truncated; stopped to avoid incomplete checks.')
        items = {x.get('content', {}).get('url'): x for x in listed['items']}
        records = []
        protected = []
        for row in rows:
            old = choose(existing, row['title'])
            wanted = row['status_column']
            if wanted == 'Needs Review' and not review_available:
                wanted = 'Todo'
            if old and is_confirmed(old, confirmed):
                protected.append(row['title'])
                url = old['html_url']
                item = items.get(url)
                actual = (item or {}).get('status', 'Not set')
                log.append(f'- Manually confirmed item kept unchanged: {url}')
                wanted = actual
            else:
                body_file = target / '.issue-body.tmp'
                wanted_body = merge_execution_plan(row['body'], (old or {}).get('body'))
                body_file.write_text(wanted_body, encoding='utf-8')
                try:
                    if old:
                        url = old['html_url']
                        change = []
                        if normalize_body(old.get('body')) != normalize_body(wanted_body):
                            change += ['--body-file', str(body_file)]
                        want_labels = desired_labels(old, row)
                        for name in sorted(want_labels - label_set(old)):
                            change += ['--add-label', name]
                        for name in sorted(label_set(old) - want_labels):
                            change += ['--remove-label', name]
                        if change:
                            run.gh('issue', 'edit', str(old['number']), '--repo', repository, *change)
                        else:
                            log.append(f'- Issue body and labels unchanged; skipped: {url}')
                    else:
                        command = ['issue', 'create', '--repo', repository, '--title', row['title'], '--body-file', str(body_file)]
                        for label in row['labels'].split(','):
                            command += ['--label', label]
                        # No assignee is ever inferred; this package was built with no nickname mapping.
                        url = run.gh(*command).splitlines()[-1].strip()
                        if not re.fullmatch(r'https://[^/]+/[^/]+/[^/]+/issues/\d+', url):
                            raise RuntimeError('gh did not return a verifiable issue URL.')
                        existing.append({'title': row['title'], 'html_url': url, 'number': int(url.rsplit('/', 1)[1]),
                                         'body': row['body'], 'labels': row['labels'].split(',')})
                    item = items.get(url)
                    if item is None:
                        item = run.gh('project', 'item-add', number, '--owner', owner, '--url', url,
                                      '--format', 'json', json_result=True)
                        items[url] = item
                    if needs_move(item, wanted):
                        run.gh('project', 'item-edit', '--id', item['id'], '--project-id', project['id'],
                               '--field-id', field['id'], '--single-select-option-id', options[wanted.casefold()])
                        item['status'] = wanted
                    else:
                        log.append(f'- Status unchanged; card not moved: {url}')
                finally:
                    body_file.unlink(missing_ok=True)
            tid = re.search(r'wechat-task:(T\d+)', row['body']).group(1)
            body_owner = re.search(r'## Recorded owner\n\n(.*?)\n\n', row['body'], re.S).group(1)
            body_status = re.search(r'## Status\n\n(.*?)\n\n', row['body'], re.S).group(1)
            records.append({'id': tid, 'title': row['title'], 'issue': url, 'status': 'Manually confirmed; unchanged' if row['title'] in protected else body_status,
                            'column': wanted, 'owner': 'Manually confirmed; unchanged' if row['title'] in protected else body_owner})
        verified = run.gh('project', 'item-list', number, '--owner', owner, '--limit', '10000',
                          '--format', 'json', json_result=True)
        verified_items = {x.get('content', {}).get('url'): x for x in verified['items']}
        for record in records:
            if record['title'] in protected:
                continue
            actual = verified_items.get(record['issue'])
            if not actual or needs_move(actual, record['column']):
                raise RuntimeError('Status read-back failed: ' + record['issue'])
        manifest = (HERE / 'manifest.md').read_text(encoding='utf-8')
        manifest = replace_table(manifest, records)
        manifest = re.sub(r'<!-- confirmed-titles: .*? -->', '<!-- confirmed-titles: ' + json.dumps(confirmed, ensure_ascii=False) + ' -->', manifest)
        manifest += f'\n\n## Import results\n\nProject: {project["url"]}\n\nAccount: {account}; Repository: {repository}.\n\nSeparate Needs Review column available: {review_available}.\n'
        manifest += '\nManually confirmed items kept unchanged: ' + ('; '.join(protected) or 'None') + '.\n'
        (target / 'manifest.md').write_text(manifest, encoding='utf-8')
        audit_base = (HERE / 'audit.md').read_text(encoding='utf-8')
        (target / 'audit.md').write_text(audit_base + '\n' + '\n'.join(log) + '\n', encoding='utf-8')
        run.run('git', 'add', '--', *(str(Path('board') / x) for x in FILES), cwd=clone)
        run.run('git', 'commit', '-m', 'Add evidence-based WeChat task board records', cwd=clone)
        run.run('git', 'push', '-u', 'origin', branch, cwd=clone)
        counts = Counter(r['column'] for r in records)
        completed = sum('status:completed' in r['labels'].split(',') for r in rows)
        needs_review = [r['title'] for r in rows if 'needs-review' in r['labels'].split(',')]
        audit_stats = re.search(r'```json\n(.*?)\n```', audit_base, re.S)
        skipped = json.loads(audit_stats.group(1))['unique_skipped_items'] if audit_stats else 'See manifest'
        body = (f'Import WeChat tasks into a native GitHub board.\n\nProject: {project["url"]}\n\n'
                f'Total tasks: {len(records)}.Board columns: {dict(counts)}.\n\n'
                f'Source extraction: completed {completed}; unfinished {len(rows)-completed}; needs review {len(needs_review)} (overlaps with source completion status).\n\n'
                f'Unique skipped items: {skipped}; six overlapping screenshot messages were deduplicated separately.\n\n'
                'See board/manifest.md for unresolved ownership, scope conflicts, time anchors, exclusions and judgments.'
                '\n\nThe original environment lacked gh; this package was imported on an authenticated machine. Screenshots and full OCR were not committed.'
                '\n\nManually confirmed items were preserved; no assignees were inferred.'
                '\n\nItems requiring manual confirmation:\n' + '\n'.join('- ' + title for title in needs_review))
        pr_body = clone / '.wechat-pr-body.tmp'
        pr_body.write_text(body, encoding='utf-8')
        try:
            pr = run.gh('pr', 'create', '--repo', repository, '--base', base, '--head', branch,
                        '--title', 'WeChat task board and evidence', '--body-file', str(pr_body))
        finally:
            pr_body.unlink(missing_ok=True)
        # Include git/push/PR command outcomes without modifying the default branch.
        (target / 'audit.md').write_text(audit_base + '\n' + '\n'.join(log) + '\n', encoding='utf-8')
        run.run('git', 'add', '--', 'board/audit.md', cwd=clone)
        run.run('git', 'commit', '-m', 'Record import and pull request results', cwd=clone)
        run.run('git', 'push', cwd=clone)
        print(json.dumps({'project': project['url'], 'pr': pr, 'task_count': len(records),
                          'clone': str(clone), 'branch': branch}, ensure_ascii=False, indent=2))
        return 0
    finally:
        # Even failed imports retain the actual command log and clone location for recovery.
        if clone:
            log.append(f'- Isolated local clone retained at `{clone}`; not deleted.')
        local_audit = HERE / 'audit.md'
        local_audit.write_text(local_audit.read_text(encoding='utf-8') + '\n' + '\n'.join(log) + '\n', encoding='utf-8')


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, OSError) as exc:
        print('Stopped: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
