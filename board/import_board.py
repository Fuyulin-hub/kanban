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
TITLE = '群聊任务看板'
MANAGED = {'source:群聊', 'needs-review', 'status:已完成', 'status:未完成', 'status:进行中'}
FILES = ('issues.csv', 'setup.sh', 'import_board.py', 'manifest.md', 'audit.md')
TABLE_START = '<!-- TASK_TABLE_START -->'
TABLE_END = '<!-- TASK_TABLE_END -->'


def load_rows(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ['title', 'body', 'labels', 'status_column']:
            raise ValueError('CSV字段必须严格为 title,body,labels,status_column')
        rows = list(reader)
    seen = set()
    for row in rows:
        if not row['title'].startswith('[群聊] ') or row['title'] in seen:
            raise ValueError('标题前缀错误或CSV中存在重复标题')
        seen.add(row['title'])
        labels = set(filter(None, row['labels'].split(',')))
        if not labels <= MANAGED or 'source:群聊' not in labels:
            raise ValueError('出现未知标签或缺少来源标签')
        if sum(x.startswith('status:') for x in labels) != 1:
            raise ValueError('每条任务必须恰有一个状态标签')
        if row['status_column'] not in {'Todo', 'In Progress', 'Done', '待确认'}:
            raise ValueError('未知看板列')
        if ('needs-review' in labels) != (row['status_column'] == '待确认'):
            raise ValueError('待确认列与needs-review不一致')
        if '负责人\n\n未指派' in row['body'] and 'needs-review' not in labels:
            raise ValueError('未指派任务必须待确认')
        for heading in ('负责人', '状态', '判定依据', '来源文件', '置信度', '待确认原因'):
            if f'## {heading}\n' not in row['body']:
                raise ValueError('Issue正文结构不完整')
        if re.search(r'(?<!\d)1[3-9]\d{9}(?!\d)', row['body']):
            raise ValueError('检测到可能未脱敏的手机号')
        if not re.search(r'<!-- wechat-task:T\d+ -->', row['body']):
            raise ValueError('缺少稳定任务编号')
    return rows


def choose(existing, title):
    hits = [x for x in existing if x.get('title') == title and not x.get('pull_request')]
    if len(hits) > 1:
        raise RuntimeError(f'仓库已有多个同名Issue，需人工去重：{title}')
    return hits[0] if hits else None


def label_set(issue):
    return {x['name'] if isinstance(x, dict) else x for x in issue.get('labels', [])}


def normalize_body(body):
    return (body or '').replace('\r\n', '\n').rstrip('\n')


def desired_labels(old, row):
    return (label_set(old) - MANAGED) | set(row['labels'].split(','))


def is_confirmed(issue, titles):
    return (issue['title'] in titles or
            bool(label_set(issue) & {'manual-confirmed', '人工确认'}) or
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
            self.log.append('  - 错误：' + safe[:1600].replace('\n', ' / '))
            if not allowed_failure:
                raise RuntimeError(safe or f'命令失败：{command[0]}')
            return None
        if json_result:
            value = json.loads(p.stdout)
            summary = f'JSON {type(value).__name__}'
            if isinstance(value, list):
                summary += f'，{len(value)}条顶层记录'
            elif isinstance(value, dict):
                summary += '，字段 ' + ', '.join(value.keys())[:250]
                if value.get('errors'):
                    self.log.append('  - GraphQL errors：' + json.dumps(value['errors'], ensure_ascii=False)[:1000])
                    if allowed_failure:
                        return None
                    raise RuntimeError('GraphQL返回errors，已停止')
            self.log.append('  - ' + summary + '；不将无关仓库正文写入审计文件。')
            return value
        self.log.append('  - ' + (p.stdout.strip()[:350].replace('\n', ' / ') or '成功，无标准输出'))
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
        raise RuntimeError('未验证到原生Board视图，不宣称看板已完成')


def status_field(run, number, owner):
    result = run.gh('project', 'field-list', number, '--owner', owner,
                    '--limit', '1000', '--format', 'json', json_result=True)
    fields = [f for f in result['fields'] if f.get('name') == 'Status']
    if len(fields) != 1 or 'options' not in fields[0]:
        raise RuntimeError('没有唯一的单选Status字段，请先在项目中配置Status')
    return fields[0]


def ensure_review_option(run, field, log):
    if any(x['name'] == '待确认' for x in field['options']):
        return True
    schema = run.graphql('query{__type(name:"ProjectV2SingleSelectFieldOptionInput"){inputFields{name}}}', {}, True)
    if not schema or 'id' not in {x['name'] for x in schema['data']['__type']['inputFields']}:
        log.append('- 待确认列降级：无法保证保留原选项ID，使用 needs-review + Todo。')
        return False
    info = run.graphql('''query($id:ID!){node(id:$id){... on ProjectV2SingleSelectField{
      id options{id name color description}}}}''', {'id': field['id']}, True)
    if not info:
        log.append('- 待确认列降级：无权读取完整选项，使用 needs-review + Todo。')
        return False
    options = info['data']['node']['options']
    # Existing IDs are essential: omitting them can clear existing project item values.
    new = options + [{'name': '待确认', 'color': 'ORANGE', 'description': '负责人、状态或范围需要人工确认'}]
    result = run.graphql('''mutation($input:UpdateProjectV2FieldInput!){updateProjectV2Field(input:$input){
      projectV2Field{... on ProjectV2SingleSelectField{id options{id name}}}}}''',
                         {'input': {'fieldId': field['id'], 'singleSelectOptions': new}}, True)
    if not result:
        log.append('- 待确认列降级：GraphQL无法添加选项，使用 needs-review + Todo。')
        return False
    return True


def replace_table(manifest, records):
    lines = ['| 编号 | 任务 | Issue | 状态 | 看板列 | 负责人 |',
             '| --- | --- | --- | --- | --- | --- |']
    for record in records:
        safe = lambda value: str(value).replace('|', '\\|').replace('\n', ' ')
        lines.append('| ' + ' | '.join(safe(record[x]) for x in ('id', 'title', 'issue', 'status', 'column', 'owner')) + ' |')
    return manifest.split(TABLE_START)[0] + TABLE_START + '\n' + '\n'.join(lines) + '\n' + TABLE_END + manifest.split(TABLE_END)[1]


def main(argv=None):
    parser = argparse.ArgumentParser(description='从已脱敏任务CSV导入GitHub原生看板，并仅提交board文件的PR')
    parser.add_argument('--repo', default='Fuyulin-hub/kanban')
    parser.add_argument('--validate-only', action='store_true', help='只验证本地CSV，不调用gh或git')
    args = parser.parse_args(argv)
    rows = load_rows(HERE / 'issues.csv')
    if args.validate_only:
        print(json.dumps({'tasks': len(rows), 'columns': dict(Counter(r['status_column'] for r in rows)),
                          'validation': 'PASS', 'external_writes': 0}, ensure_ascii=False, indent=2))
        return 0
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', args.repo):
        raise ValueError('--repo应为owner/repo')
    log = ['\n## 登录机器执行日志', '', f'UTC开始时间 {dt.datetime.now(dt.timezone.utc).isoformat()}']
    run = Runner(log)
    clone = None
    try:
        # Required sequence. Any failure here stops immediately; no alternate connector/API is used.
        if not shutil.which('gh'):
            raise RuntimeError('找不到gh；请先安装GitHub CLI、登录并授予project权限。')
        run.gh('--version')
        run.gh('auth', 'status')
        run.gh('project', 'list', '--limit', '1')
        repo = run.gh('repo', 'view', args.repo, '--json', 'nameWithOwner,owner,defaultBranchRef', json_result=True)
        account = run.gh('api', 'user', '--jq', '.login')
        account_id = run.gh('api', 'user', '--jq', '.id')
        owner = repo['owner']['login']
        repository = repo['nameWithOwner']
        if not (repo.get('defaultBranchRef') or {}).get('name'):
            raise RuntimeError('目标仓库为空。请先在GitHub网页创建README以初始化默认分支；脚本不会直接推main或替你创建基础提交。')
        base = repo['defaultBranchRef']['name']
        if not shutil.which('git'):
            raise RuntimeError('缺少git，不能提交PR。')
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
            raise RuntimeError('项目列表被截断，停止以避免重复建项目。')
        hits = [p for p in projects['projects'] if p['title'] == TITLE]
        if len(hits) > 1:
            raise RuntimeError('同名Project不唯一，请人工指定或去重。')
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
                raise RuntimeError('Status缺少必需选项：' + status)
        if review_available and '待确认' not in options:
            raise RuntimeError('待确认选项创建后未通过读取校验。')
        labels = flatten_pages(run.gh('api', '--paginate', '--slurp', f'repos/{repository}/labels?per_page=100', json_result=True))
        known_labels = {x['name'] for x in labels}
        for name in sorted(MANAGED - known_labels):
            run.gh('label', 'create', name, '--repo', repository,
                   '--color', 'd4c5f9' if name == 'needs-review' else 'd9eaf7')
        listed = run.gh('project', 'item-list', number, '--owner', owner, '--limit', '10000',
                        '--format', 'json', json_result=True)
        if listed.get('totalCount', 0) > len(listed['items']):
            raise RuntimeError('项目条目被截断，停止以避免漏查。')
        items = {x.get('content', {}).get('url'): x for x in listed['items']}
        records = []
        protected = []
        for row in rows:
            old = choose(existing, row['title'])
            wanted = row['status_column']
            if wanted == '待确认' and not review_available:
                wanted = 'Todo'
            if old and is_confirmed(old, confirmed):
                protected.append(row['title'])
                url = old['html_url']
                item = items.get(url)
                actual = (item or {}).get('status', '未设置')
                log.append(f'- 人工确认条目保持不变：{url}')
                wanted = actual
            else:
                body_file = target / '.issue-body.tmp'
                body_file.write_text(row['body'], encoding='utf-8')
                try:
                    if old:
                        url = old['html_url']
                        change = []
                        if normalize_body(old.get('body')) != normalize_body(row['body']):
                            change += ['--body-file', str(body_file)]
                        want_labels = desired_labels(old, row)
                        for name in sorted(want_labels - label_set(old)):
                            change += ['--add-label', name]
                        for name in sorted(label_set(old) - want_labels):
                            change += ['--remove-label', name]
                        if change:
                            run.gh('issue', 'edit', str(old['number']), '--repo', repository, *change)
                        else:
                            log.append(f'- Issue正文和标签未变化，跳过更新：{url}')
                    else:
                        command = ['issue', 'create', '--repo', repository, '--title', row['title'], '--body-file', str(body_file)]
                        for label in row['labels'].split(','):
                            command += ['--label', label]
                        # No assignee is ever inferred; this package was built with no nickname mapping.
                        url = run.gh(*command).splitlines()[-1].strip()
                        if not re.fullmatch(r'https://[^/]+/[^/]+/[^/]+/issues/\d+', url):
                            raise RuntimeError('gh未返回可验证的Issue URL。')
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
                        log.append(f'- Status未变化，不移动列：{url}')
                finally:
                    body_file.unlink(missing_ok=True)
            tid = re.search(r'wechat-task:(T\d+)', row['body']).group(1)
            body_owner = re.search(r'## 负责人\n\n(.*?)\n\n', row['body'], re.S).group(1)
            body_status = re.search(r'## 状态\n\n(.*?)\n\n', row['body'], re.S).group(1)
            records.append({'id': tid, 'title': row['title'], 'issue': url, 'status': '人工确认 保持原状' if row['title'] in protected else body_status,
                            'column': wanted, 'owner': '人工确认 保持原状' if row['title'] in protected else body_owner})
        verified = run.gh('project', 'item-list', number, '--owner', owner, '--limit', '10000',
                          '--format', 'json', json_result=True)
        verified_items = {x.get('content', {}).get('url'): x for x in verified['items']}
        for record in records:
            if record['title'] in protected:
                continue
            actual = verified_items.get(record['issue'])
            if not actual or needs_move(actual, record['column']):
                raise RuntimeError('写入后Status核对失败：' + record['issue'])
        manifest = (HERE / 'manifest.md').read_text(encoding='utf-8')
        manifest = replace_table(manifest, records)
        manifest = re.sub(r'<!-- confirmed-titles: .*? -->', '<!-- confirmed-titles: ' + json.dumps(confirmed, ensure_ascii=False) + ' -->', manifest)
        manifest += f'\n\n## 实际导入结果\n\nProject：{project["url"]}\n\n账号：{account}；仓库：{repository}。\n\n待确认独立列可用：{review_available}。\n'
        manifest += '\n人工确认而保持不变的条目：' + ('；'.join(protected) or '无') + '。\n'
        (target / 'manifest.md').write_text(manifest, encoding='utf-8')
        audit_base = (HERE / 'audit.md').read_text(encoding='utf-8')
        (target / 'audit.md').write_text(audit_base + '\n' + '\n'.join(log) + '\n', encoding='utf-8')
        run.run('git', 'add', '--', *(str(Path('board') / x) for x in FILES), cwd=clone)
        run.run('git', 'commit', '-m', 'Add evidence-based WeChat task board records', cwd=clone)
        run.run('git', 'push', '-u', 'origin', branch, cwd=clone)
        counts = Counter(r['column'] for r in records)
        completed = sum('status:已完成' in r['labels'].split(',') for r in rows)
        needs_review = [r['title'] for r in rows if 'needs-review' in r['labels'].split(',')]
        audit_stats = re.search(r'```json\n(.*?)\n```', audit_base, re.S)
        skipped = json.loads(audit_stats.group(1))['跳过的不同条目合计'] if audit_stats else '见manifest'
        body = (f'将群聊任务导入GitHub原生看板。\n\nProject：{project["url"]}\n\n'
                f'任务总数：{len(records)}。看板列分布：{dict(counts)}。\n\n'
                f'本批提取标注：已完成{completed}；未完成{len(rows)-completed}；待确认{len(needs_review)}（与完成状态为不同维度）。\n\n'
                f'跳过的不同条目：{skipped}；另去除6条截图重叠消息。\n\n'
                '未指派、范围冲突、时间锚点、跳过统计及主观判定见board/manifest.md。'
                '\n\n初次环境缺少gh，故由降级包在本机导入。原始截图、OCR全文未进入仓库。'
                '\n\n已保留人工确认条目；未给任何Issue自动设置assignee。'
                '\n\n无法自动判定的条目：\n' + '\n'.join('- ' + title for title in needs_review))
        pr_body = clone / '.wechat-pr-body.tmp'
        pr_body.write_text(body, encoding='utf-8')
        try:
            pr = run.gh('pr', 'create', '--repo', repository, '--base', base, '--head', branch,
                        '--title', '群聊任务看板与判定依据', '--body-file', str(pr_body))
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
            log.append(f'- 本地隔离克隆保留于 `{clone}`；未删除。')
        local_audit = HERE / 'audit.md'
        local_audit.write_text(local_audit.read_text(encoding='utf-8') + '\n' + '\n'.join(log) + '\n', encoding='utf-8')


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, OSError) as exc:
        print('停止：' + str(exc), file=sys.stderr)
        raise SystemExit(1)
