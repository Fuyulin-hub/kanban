# Execution audit

## Source accounting

```json
{
  "unique_inspected_items": 412,
  "evidence_message_bubbles": 85,
  "skipped_media": 93,
  "other_text_not_separate_tasks": 224,
  "system_notifications": 10,
  "unique_skipped_items": 327,
  "overlap_duplicates_removed": 6
}
```

## Authorization and previous work

- The user requested an evidence-based GitHub Projects board for Fuyulin-hub/kanban, then authorized execution recommendations, workstreams and the four confirmed member names.
- The user authorized one README-only initialization of the empty main branch. Its commit is ebcc3033b2d2c9ca7eba4bb63849377521eefb5a. Subsequent board files were submitted through feature branches and PR #49.
- Official GitHub CLI device OAuth was used. No credential pasted into chat was used or stored.
- The original import created 48 issues and the project, kept assignees empty and recorded four completed tasks. Later additions created seven workstream views and four proposed-lead views.
- Prior import/enrichment logs and the earlier-language snapshots remain traceable through the PR commit history, including c2def9913055b405e74cabfa4f3a531cebdc0438. This file is the English current-version audit, not a rewrite of historical commits.

## English conversion requested on 2026-11-03

- Removed the screenshot-style speaker field and its explanatory identity annotations. Visible card fields now focus on Title, Status, Workstream and Suggested lead.
- Converted project title, description, README, view names, status option names, custom-field names/options, labels, issue titles/bodies and documentation to English. Member names use pinyin.
- Kept issue URLs/numbers, item IDs, label identities and existing status/select-option IDs. Only the requested speaker-provenance field was deleted.
- Source excerpts are explicitly labeled English translations. Stable task/message IDs, source filenames, uncertainty and nearby time anchors remain; the original-language local records were not modified or committed.
- Updated CSV/importer terminology to match the live English titles and labels, retaining the plan-preservation and manual-confirmation behavior.
- One field-deletion query initially named an unsupported response field and was rejected before mutation. The corrected request succeeded; no issue or status was deleted.

## Read-back verification

- 48 issues and 48 project items remain. All titles/bodies and current project metadata are English.
- All issue states and GitHub assignees match the pre-conversion snapshot. Status option IDs remain identical.
- Columns: Todo 6, In Progress 2, Done 4, Needs Review 36. The renamed review column retains its 36 existing cards.
- All workstream and proposed-lead values match their translated plans. Recorded-owner text no longer contains the removed identity/nickname annotations.
- Each issue contains exactly one execution-plan block. No Chinese characters remain in current issue bodies/titles, labels or project metadata.
- The CSV validates locally with zero external writes; three packaged plan-preservation regression tests and 12 complete offline behavior tests pass. A failing offline run exposed an English-label case-folding lookup; the lookup was corrected and all 12 tests passed.

## Mutation results

- Renamed the project and updated its description and README in English.
- Updated field: Status; existing option IDs preserved.
- Updated field: Workstream; existing option IDs preserved.
- Updated field: Suggested lead; existing option IDs preserved.
- Updated field: Recorded owner; existing option IDs preserved.
- Renamed label: source:wechat
- Renamed label: status:completed
- Renamed label: status:unfinished
- Renamed label: status:in-progress
- Renamed label: module:requirements
- Renamed label: module:report
- Renamed label: module:data
- Renamed label: module:formatting
- Renamed label: module:website
- Renamed label: module:presentation
- Renamed label: module:submission
- Renamed label: suggested-lead:zhang-xinyue
- Renamed label: suggested-lead:xu-jiale
- Renamed label: suggested-lead:wang-siqi
- Renamed label: suggested-lead:fu-yulin
- Updated view: All Tasks
- Updated view: Task Board
- Updated view: Requirements & References
- Updated view: Report & Translation
- Updated view: Data & Figures
- Updated view: Formatting & Compilation
- Updated view: Slides & Presentation
- Updated view: Website & Deployment
- Updated view: Submission & Delivery
- Updated view: Zhang Xinyue - Suggested Tasks
- Updated view: Xu Jiale - Suggested Tasks
- Updated view: Wang Siqi - Suggested Tasks
- Updated view: Fu Yulin - Suggested Tasks
- Renamed the project and updated its description and README in English.
- Removed the speaker-provenance field requested in the screenshot.
- updateIssue: inputs 1–10 succeeded.
- updateIssue: inputs 11–20 succeeded.
- updateIssue: inputs 21–30 succeeded.
- updateIssue: inputs 31–40 succeeded.
- updateIssue: inputs 41–48 succeeded.
- updateProjectV2ItemFieldValue: inputs 1–10 succeeded.
- updateProjectV2ItemFieldValue: inputs 11–20 succeeded.
- updateProjectV2ItemFieldValue: inputs 21–30 succeeded.
- updateProjectV2ItemFieldValue: inputs 31–40 succeeded.
- updateProjectV2ItemFieldValue: inputs 41–48 succeeded.
- Read-back passed: 48 English issues; all existing status option IDs, states and assignees preserved. {'Needs Review': 36, 'In Progress': 2, 'Done': 4, 'Todo': 6}

## GitHub CLI calls

Each line records the actual command and exit status. Structured payload files contain no credentials.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api 'repos/Fuyulin-hub/kanban/labels?per_page=100'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/source%3A%E7%BE%A4%E8%81%8A --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/status%3A%E5%B7%B2%E5%AE%8C%E6%88%90 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/status%3A%E6%9C%AA%E5%AE%8C%E6%88%90 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/status%3A%E8%BF%9B%E8%A1%8C%E4%B8%AD --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/module%3A%E8%B5%84%E6%96%99%E4%B8%8E%E9%9C%80%E6%B1%82%E6%A0%B8%E5%AF%B9 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/module%3A%E6%8A%A5%E5%91%8A%E6%AD%A3%E6%96%87%E4%B8%8E%E7%BF%BB%E8%AF%91 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/module%3A%E6%95%B0%E6%8D%AE%E5%9B%BE%E8%A1%A8%E4%B8%8E%E5%AE%9E%E9%AA%8C --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/module%3A%E6%96%87%E6%A1%A3%E6%8E%92%E7%89%88%E4%B8%8E%E7%BC%96%E8%AF%91 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/module%3A%E7%BD%91%E9%A1%B5%E4%B8%8E%E9%83%A8%E7%BD%B2 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/module%3APPT%E4%B8%8E%E7%AD%94%E8%BE%A9 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/module%3A%E6%8F%90%E4%BA%A4%E4%B8%8E%E4%BA%A4%E4%BB%98 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/%E5%BB%BA%E8%AE%AE%E6%89%A7%E8%A1%8C%E4%BA%BA%3A%E5%BC%A0%E9%A6%A8%E6%9C%88 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/%E5%BB%BA%E8%AE%AE%E6%89%A7%E8%A1%8C%E4%BA%BA%3A%E5%BE%90%E4%BD%B3%E4%B9%90 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/%E5%BB%BA%E8%AE%AE%E6%89%A7%E8%A1%8C%E4%BA%BA%3A%E7%8E%8B%E6%80%9D%E7%90%A6 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method PATCH repos/Fuyulin-hub/kanban/labels/%E5%BB%BA%E8%AE%AE%E6%89%A7%E8%A1%8C%E4%BA%BA%3A%E4%BB%98%E7%8E%89%E7%90%B3 --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 1; gh: Field 'deletedFieldId' doesn't exist on type 'DeleteProjectV2FieldPayload' / 
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api 'repos/Fuyulin-hub/kanban/labels?per_page=100'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api 'repos/Fuyulin-hub/kanban/labels?per_page=100'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.
- `gh api --method POST graphql --input 'work\enrichment_payload.json'`: exit 0.

## File publication

Current English board files are published only to the existing PR feature branch. The Git data API preserves the parent tree, updates the branch with force=false, and leaves main unchanged. Publication commit IDs, current file hashes and final PR status are recorded in the PR description and delivery receipt to avoid a self-referential audit commit.

No report editing, experiment execution, website deployment, email sending or course submission was performed.
