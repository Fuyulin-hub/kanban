# 群聊任务看板执行审计

## 实际预检与停止点

本次执行日期为2026年11月3日，时区Asia/Shanghai。目标仓库后由用户截图明确为Fuyulin-hub/kanban。

| 顺序 | 命令 | 实际结果 |
| --- | --- | --- |
| 1 | gh --version | exit 1；PowerShell提示找不到gh命令 |
| 2 | gh auth status | 未执行；前一步失败后按用户规则停止 |
| 3 | gh project list --limit 1 | 未执行；未验证登录或Projects读写权限 |
| 4 | gh repo view --json nameWithOwner,owner | 未执行；仓库名称由用户截图提供，不伪装成命令返回 |
| 5 | gh api user --jq .login | 未执行；当前GitHub账号未知 |

本地另执行git rev-parse --show-toplevel，结果exit 1，当前目录不是Git仓库。未通过浏览器、其他连接器或裸GitHub API绕过预检，未创建任何远端资源，也未提交PR。

## 已完成的本地处理

- 以只读方式读取用户提供的9张截图，在work中生成71个本地OCR切片。
- 使用Windows本机简体中文OCR；对任务引用和作者标识进行原图核对。OCR全文、切片及含隐私的消息索引仅留本地work，不进入交付包。
- 通过消息位置建立S编号和M编号，合并S5与S6重复的6条消息；4条边缘片段另以P编号记录。
- 逐项区分明确认领、被指派、完成汇报和讨论；逐项理由保存在manifest及Issue正文。
- 输出指定四列的issues.csv、setup.sh、manifest.md，另附只用标准库的导入器和本执行审计。
- 只读查询GitHub官方文档以核对gh参数和GraphQL字段；这些是公开文档查询，不是替用户操作GitHub资源。

## 统计与跳过索引

```json
{
  "任务数": 48,
  "已完成": 4,
  "未完成": 44,
  "待确认": 36,
  "互斥看板列": {
    "待确认": 36,
    "In Progress": 2,
    "Done": 4,
    "Todo": 6
  },
  "截图带完整头像气泡": 404,
  "边缘裁切但可定位气泡": 4,
  "重复气泡": 6,
  "去重后气泡": 402,
  "采用为任务依据的不同气泡": 85,
  "跳过的媒体附件表情气泡": 93,
  "未单独建任务的其他文本气泡": 224,
  "撤回通知": 9,
  "拍一拍通知": 1,
  "跳过的不同条目合计": 327,
  "去重后可定位条目总数": 412
}
```

媒体、附件、表情气泡（不含原文内容）：

S1-M003, S1-M022, S1-M025, S1-M034, S1-M035, S1-M043, S1-M045, S1-M046, S1-M047, S1-M050, S1-M051, S1-M056, S1-M059, S1-M069, S1-M070, S1-M071, S1-M072, S1-M074, S2-M011, S2-M012, S2-M013, S2-M016, S2-M020, S2-M028, S2-M029, S2-M030, S2-M031, S2-M037, S2-M038, S2-M039, S2-M040, S2-M041, S2-M043, S2-M054, S2-P001, S3-M006, S3-M008, S3-M009, S3-M011, S3-M017, S3-M018, S3-M029, S3-M030, S3-M034, S3-P001, S4-M001, S4-M016, S4-M024, S4-M025, S4-M033, S4-M034, S4-M036, S4-M038, S4-M039, S4-M042, S4-M043, S4-M044, S4-M045, S4-M047, S6-M001, S6-M003, S6-M004, S6-M005, S6-M012, S6-M016, S6-M019, S6-M030, S6-M036, S6-M040, S7-M002, S7-M025, S7-M030, S7-M037, S7-M038, S8-M001, S8-M002, S8-M005, S8-M009, S8-M011, S8-M013, S8-M022, S8-M029, S8-M030, S8-M038, S9-M004, S9-M019, S9-M027, S9-M028, S9-M033, S9-M038, S9-M039, S9-M040, S9-M044

其他未单独生成任务的文本气泡（不含原文内容）：

S1-M001, S1-M004, S1-M005, S1-M007, S1-M008, S1-M010, S1-M011, S1-M012, S1-M013, S1-M014, S1-M015, S1-M016, S1-M017, S1-M019, S1-M020, S1-M021, S1-M023, S1-M024, S1-M026, S1-M028, S1-M029, S1-M032, S1-M033, S1-M036, S1-M037, S1-M038, S1-M039, S1-M041, S1-M042, S1-M044, S1-M052, S1-M053, S1-M055, S1-M057, S1-M060, S1-M062, S1-M063, S1-M064, S1-M066, S1-M067, S1-M068, S1-M073, S2-M002, S2-M003, S2-M005, S2-M009, S2-M010, S2-M014, S2-M015, S2-M017, S2-M021, S2-M022, S2-M023, S2-M024, S2-M025, S2-M026, S2-M027, S2-M032, S2-M033, S2-M034, S2-M035, S2-M036, S2-M042, S2-M044, S2-M045, S2-M046, S2-M047, S2-M048, S2-M050, S2-M052, S2-M053, S2-M055, S2-M056, S2-M057, S2-M058, S2-M059, S2-M060, S3-M003, S3-M005, S3-M012, S3-M013, S3-M014, S3-M015, S3-M016, S3-M019, S3-M020, S3-M021, S3-M022, S3-M024, S3-M025, S3-M026, S3-M027, S3-M028, S3-M033, S3-M035, S3-M036, S3-M037, S3-M038, S4-M002, S4-M004, S4-M005, S4-M006, S4-M007, S4-M008, S4-M010, S4-M011, S4-M012, S4-M013, S4-M014, S4-M015, S4-M019, S4-M022, S4-M023, S4-M028, S4-M030, S4-M031, S4-M032, S4-M037, S4-M046, S6-M002, S6-M007, S6-M009, S6-M010, S6-M011, S6-M013, S6-M015, S6-M017, S6-M021, S6-M022, S6-M023, S6-M024, S6-M027, S6-M032, S6-M033, S6-M034, S6-M037, S6-M038, S6-M042, S6-M043, S6-M045, S6-M046, S6-M047, S7-M001, S7-M003, S7-M004, S7-M005, S7-M006, S7-M007, S7-M008, S7-M009, S7-M010, S7-M012, S7-M013, S7-M014, S7-M015, S7-M016, S7-M019, S7-M020, S7-M022, S7-M023, S7-M024, S7-M027, S7-M029, S7-M031, S7-M035, S7-M036, S7-P001, S8-M003, S8-M004, S8-M006, S8-M007, S8-M010, S8-M016, S8-M017, S8-M019, S8-M021, S8-M023, S8-M024, S8-M025, S8-M026, S8-M027, S8-M028, S8-M031, S8-M032, S8-M033, S8-M034, S8-M035, S8-M036, S8-M037, S8-M040, S8-M041, S8-M042, S8-M044, S9-M001, S9-M002, S9-M003, S9-M005, S9-M007, S9-M008, S9-M009, S9-M010, S9-M011, S9-M012, S9-M013, S9-M014, S9-M015, S9-M016, S9-M018, S9-M020, S9-M021, S9-M022, S9-M023, S9-M025, S9-M029, S9-M030, S9-M031, S9-M032, S9-M035, S9-M036, S9-M037, S9-M041, S9-M042, S9-M043, S9-M046

重叠截图消息：

S5-M001 = S6-M001, S5-M002 = S6-M002, S5-M003 = S6-M003, S5-M004 = S6-M004, S5-M005 = S6-M005, S5-M006 = S6-M006

系统通知：

- 拍一拍；Screenshot_2026-11-03-09-57-34-904_com.tencent.m.jpg；y≈1507。
- 撤回；Screenshot_2026-11-03-09-57-34-904_com.tencent.m.jpg；y≈7986。
- 撤回；Screenshot_2026-11-03-09-57-34-904_com.tencent.m.jpg；y≈9649。
- 撤回；Screenshot_2026-11-03-09-57-34-904_com.tencent.m.jpg；y≈24088。
- 撤回；Screenshot_2026-11-03-10-00-10-943_com.tencent.m.jpg；y≈1856。
- 撤回；Screenshot_2026-11-03-10-00-51-753_com.tencent.m.jpg；y≈8513。
- 撤回；Screenshot_2026-11-03-10-01-29-754_com.tencent.m.jpg；y≈10760。
- 撤回；Screenshot_2026-11-03-10-02-18-689_com.tencent.m.jpg；y≈3659。
- 撤回；Screenshot_2026-11-03-10-04-06-128_com.tencent.m.jpg；y≈10219。
- 撤回；Screenshot_2026-11-03-10-04-06-128_com.tencent.m.jpg；y≈10329。

## 验证范围

本地CSV结构、引用定位、标签与列的一致性、隐私扫描、脚本语法和模拟幂等测试将记录在交付核查结果中。真实GitHub登录、Projects写权限、线上创建结果与PR均未验证；不把模拟测试写成线上运行成功。

## 本地验证结果

- 8项离线行为测试通过：CSV与状态一致、两次导入不重复、状态不变不移列、预检失败即停、空库不写入、人工确认条目保护、待确认列权限失败降级、保留原有无关标签。
- bash -n检查setup.sh通过；Python语法解析通过；48行CSV结构验证通过。
- 已扫描交付文件中的已知姓名和手机号模式，未发现未脱敏值。
- 9张原始截图的SHA256与只读处理前后记录一致。
- 上述均是本地或模拟验证，未调用真实GitHub写接口，未生成真实Project、Issue或PR。


## 登录机器执行日志

UTC开始时间 2026-11-03T03:22:24.969765+00:00
- `gh --version` → exit 0
  - gh version 2.103.3 (2026-10-26) / https://github.com/cli/cli/releases/tag/v2.103.3
- `gh auth status` → exit 0
  - github.com /   ✓ Logged in to github.com account Fuyulin-hub (keyring) /   - Active account: true /   - Git operations protocol: https /   - Token: gho_************************************ /   - Token scopes: 'gist', 'project', 'read:org', 'repo', 'workflow'
- `gh project list --limit 1` → exit 0
  - 1	@Fuyulin-hub's 3D Part Segmentation Research	open	PVT_kwHOC3MSJ84Bn1v5
- `gh repo view Fuyulin-hub/kanban --json nameWithOwner,owner,defaultBranchRef` → exit 0
  - JSON dict，字段 defaultBranchRef, nameWithOwner, owner；不将无关仓库正文写入审计文件。
- `gh api user --jq .login` → exit 0
  - Fuyulin-hub
- `gh api user --jq .id` → exit 0
  - 192090663
- `gh api --paginate --slurp 'repos/Fuyulin-hub/kanban/issues?state=all&per_page=100'` → exit 0
  - JSON list，1条顶层记录；不将无关仓库正文写入审计文件。
- `gh repo clone Fuyulin-hub/kanban 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo' -- --branch main` → exit 0
  - 成功，无标准输出
- `git config user.name Fuyulin-hub` → exit 0
  - 成功，无标准输出
- `git config user.email 192090663+Fuyulin-hub@users.noreply.github.com` → exit 0
  - 成功，无标准输出
- `git switch -c board/wechat-20261103-032234` → exit 0
  - 成功，无标准输出
- `gh project list --owner Fuyulin-hub --limit 10000 --format json` → exit 0
  - JSON dict，字段 projects, totalCount；不将无关仓库正文写入审计文件。
- `gh project create --owner Fuyulin-hub --title '群聊任务看板' --format json` → exit 0
  - JSON dict，字段 closed, fields, id, items, number, owner, public, readme, shortDescription, title, url；不将无关仓库正文写入审计文件。
- `gh project view 2 --owner Fuyulin-hub --format json` → exit 0
  - JSON dict，字段 closed, fields, id, items, number, owner, public, readme, shortDescription, title, url；不将无关仓库正文写入审计文件。
- `gh api graphql --input 'C:\Users\ASUS\AppData\Local\Temp\tmpoqz_hguc.json'` → exit 0
  - JSON dict，字段 data；不将无关仓库正文写入审计文件。
- `gh api graphql --input 'C:\Users\ASUS\AppData\Local\Temp\tmp2abgb4bf.json'` → exit 0
  - JSON dict，字段 data；不将无关仓库正文写入审计文件。
- `gh api graphql --input 'C:\Users\ASUS\AppData\Local\Temp\tmp3wurxil4.json'` → exit 0
  - JSON dict，字段 data；不将无关仓库正文写入审计文件。
- `gh project field-list 2 --owner Fuyulin-hub --limit 1000 --format json` → exit 0
  - JSON dict，字段 fields, totalCount；不将无关仓库正文写入审计文件。
- `gh api graphql --input 'C:\Users\ASUS\AppData\Local\Temp\tmp9xqn9jlb.json'` → exit 0
  - JSON dict，字段 data；不将无关仓库正文写入审计文件。
- `gh api graphql --input 'C:\Users\ASUS\AppData\Local\Temp\tmpaz8gcz0b.json'` → exit 0
  - JSON dict，字段 data；不将无关仓库正文写入审计文件。
- `gh api graphql --input 'C:\Users\ASUS\AppData\Local\Temp\tmphi5iqtyj.json'` → exit 0
  - JSON dict，字段 data；不将无关仓库正文写入审计文件。
- `gh project field-list 2 --owner Fuyulin-hub --limit 1000 --format json` → exit 0
  - JSON dict，字段 fields, totalCount；不将无关仓库正文写入审计文件。
- `gh api --paginate --slurp 'repos/Fuyulin-hub/kanban/labels?per_page=100'` → exit 0
  - JSON list，1条顶层记录；不将无关仓库正文写入审计文件。
- `gh label create needs-review --repo Fuyulin-hub/kanban --color d4c5f9` → exit 0
  - 成功，无标准输出
- `gh label create 'source:群聊' --repo Fuyulin-hub/kanban --color d9eaf7` → exit 0
  - 成功，无标准输出
- `gh label create 'status:已完成' --repo Fuyulin-hub/kanban --color d9eaf7` → exit 0
  - 成功，无标准输出
- `gh label create 'status:未完成' --repo Fuyulin-hub/kanban --color d9eaf7` → exit 0
  - 成功，无标准输出
- `gh label create 'status:进行中' --repo Fuyulin-hub/kanban --color d9eaf7` → exit 0
  - 成功，无标准输出
- `gh project item-list 2 --owner Fuyulin-hub --limit 10000 --format json` → exit 0
  - JSON dict，字段 items, totalCount；不将无关仓库正文写入审计文件。
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 获取上一年的参考报告' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/1
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/1 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkx3w --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 核对报告正文内容' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:进行中' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/2
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/2 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkx8A --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 规划并细化报告图表' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:进行中'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/3
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/3 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkyB0 --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id 47fc9ee4` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 修订报告前三章' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:进行中' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/4
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/4 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkyGo --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 标注报告图表的插入位置' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:已完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/5
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/5 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkyLk --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id 98236657` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 核查真实数据的缺失率' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/6
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/6 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkyPs --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 在报告前三章补充相关元素的图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/7
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/7 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkyUk --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 调整报告中数据缺失的表述' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/8
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/8 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkyaE --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id f75ad846` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 完成报告的首次编译' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:已完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/9
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/9 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkyes --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id 98236657` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 制作小组汇报PPT' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/10
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/10 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkykg --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 在PPT中说明人员分工' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/11
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/11 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkypo --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 绘制第七章项目实施计划甘特图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/12
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/12 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkyxg --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id f75ad846` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 为计划提交物设计可视化前端网页并提供截图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/13
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/13 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFky1k --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 整合各章形成完整报告' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:进行中'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/14
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/14 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFky70 --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id 47fc9ee4` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 细化并排版汇报PPT' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/15
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/15 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzCQ --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 查找老师规定的具体提交时间' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/16
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/16 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzHk --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 美化已讨论的鱼骨图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/17
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/17 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzLw --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id f75ad846` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 在报告中补充第七章' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:已完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/18
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/18 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzQE --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id 98236657` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 修改可视化网页及配色' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:已完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/19
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/19 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzVE --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id 98236657` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 准备课堂汇报稿' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/20
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/20 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzYo --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 再次人工检查并改写报告的AI式表达' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/21
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/21 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzeI --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 检查报告还需要哪些图表并补入' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/22
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/22 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzog --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id f75ad846` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 按老师课件措辞将报告翻译为英文' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:进行中' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/23
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/23 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzs0 --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 美化并排版整份报告' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:进行中' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/24
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/24 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkzxM --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 在英文报告中重新插入封面' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/25
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/25 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFkz4Y --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 美化所指的风险评分流程图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/26
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/26 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0AI --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 修正鱼骨图内容并调整至第四章' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/27
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/27 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0Is --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 在第四章补充两张数据预处理图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/28
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/28 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0Qo --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 制作订单分群的可视化图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/29
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/29 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0V4 --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 制作类别联购的可视化图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/30
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/30 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0bg --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 制作葡语评论分析的可视化图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/31
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/31 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0gQ --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 裁切图表以适配PPT版面' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/32
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/32 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0kQ --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 将可视化网页部署为他人可访问的网站' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/33
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/33 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0oY --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 处理英文报告的目录生成问题' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:进行中' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/34
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/34 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0sI --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 提供英文报告的LaTeX源码' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/35
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/35 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk0xQ --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 进行二次编译以生成报告目录' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/36
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/36 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk01s --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 在美化前检查英文报告及源码' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/37
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/37 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk05U --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 制作缺失率的可视化' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/38
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/38 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk094 --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 核实小组作业由几人提交' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/39
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/39 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1Bs --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 通过邮件提交Project Proposal' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/40
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/40 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1Lw --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 确认并执行Moodle提交流程' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/41
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/41 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1QQ --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 精简新增图表的图注' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/42
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/42 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1T4 --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 删除报告中所指的四个括号' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/43
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/43 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1YA --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 寻找并选择与封面协调的报告背景图' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/44
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/44 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1dE --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 将候选背景插入报告试排' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/45
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/45 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1jE --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id f75ad846` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 用汇报PPT准备辅助答疑' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/46
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/46 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1oc --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id f75ad846` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 将网页链接加入汇报PPT' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/47
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/47 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1tQ --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh issue create --repo Fuyulin-hub/kanban --title '[群聊] 安排并参加课堂小组汇报' --body-file 'C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo\board\.issue-body.tmp' --label 'source:群聊' --label 'status:未完成' --label needs-review` → exit 0
  - https://github.com/Fuyulin-hub/kanban/issues/48
- `gh project item-add 2 --owner Fuyulin-hub --url https://github.com/Fuyulin-hub/kanban/issues/48 --format json` → exit 0
  - JSON dict，字段 body, id, title, type, url；不将无关仓库正文写入审计文件。
- `gh project item-edit --id PVTI_lAHOC3MSJ84Bp7xgzhFk1yM --project-id PVT_kwHOC3MSJ84Bp7xg --field-id PVTSSF_lAHOC3MSJ84Bp7xgzhoVGzo --single-select-option-id c9982180` → exit 0
  - 成功，无标准输出
- `gh project item-list 2 --owner Fuyulin-hub --limit 10000 --format json` → exit 0
  - JSON dict，字段 items, totalCount；不将无关仓库正文写入审计文件。
- `git add -- 'board\issues.csv' 'board\setup.sh' 'board\import_board.py' 'board\manifest.md' 'board\audit.md'` → exit 0
  - 成功，无标准输出
- `git commit -m 'Add evidence-based WeChat task board records'` → exit 0
  - [board/wechat-20261103-032234 60fd35a] Add evidence-based WeChat task board records /  5 files changed, 2636 insertions(+) /  create mode 100644 board/audit.md /  create mode 100644 board/import_board.py /  create mode 100644 board/issues.csv /  create mode 100644 board/manifest.md /  create mode 100644 board/setup.sh
- `git push -u origin board/wechat-20261103-032234` → exit 128
  - 错误：fatal: unable to access 'https://github.com/Fuyulin-hub/kanban.git/': Failed to connect to github.com:443 after 21119 ms: Could not connect to server
- 本地隔离克隆保留于 `C:\Users\ASUS\AppData\Local\Temp\wechat-board-pi6wfre1\repo`；未删除。

## 后续授权与初始化

- 官方GitHub CLI便携程序已下载，并按官方发布资产SHA256核对。
- 第一次浏览器授权后的本机网络交换超时；第二次官方设备登录成功，账号Fuyulin-hub，凭据保存在系统keyring。没有使用或保存用户贴到聊天中的令牌。
- 已重新通过gh --version、gh auth status、gh project list --limit 1、gh repo view及gh api user检查。
- 用户明确允许一次初始化main。仅提交README.md，提交SHA ebcc3033b2d2c9ca7eba4bb63849377521eefb5a；任务记录不写main。
- gh project link 2 --owner Fuyulin-hub --repo Fuyulin-hub/kanban → exit 0，项目已关联目标仓库。
- 10项离线行为测试通过，包含空仓库返回空name应停止，以及GitHub返回CRLF换行时不误更新正文。

## Git传输失败后的提交恢复

48条Issue及其Status已全部创建并读回。git push因github.com:443连接失败退出128，尚未创建PR。后续使用已通过预检的同一个gh登录态，经GitHub Git数据接口将同样5个board文件写入功能分支，然后创建PR。未更换身份、未重建Issue、未推送任务文件到main。

## GitHub接口恢复结果

- `gh api 'repos/Fuyulin-hub/kanban/issues?state=all&per_page=100'` → exit 0
  - 48条记录
- `gh project item-list 2 --owner Fuyulin-hub --format json --limit 100` → exit 0
  - {"keys": ["items", "totalCount"]}
- `gh api repos/Fuyulin-hub/kanban/git/ref/heads/main` → exit 0
  - {"ref": "refs/heads/main"}
- `gh api repos/Fuyulin-hub/kanban/git/commits/ebcc3033b2d2c9ca7eba4bb63849377521eefb5a` → exit 0
  - {"sha": "ebcc3033b2d2c9ca7eba4bb63849377521eefb5a", "html_url": "https://github.com/Fuyulin-hub/kanban/commit/ebcc3033b2d2c9ca7eba4bb63849377521eefb5a"}
- `gh api repos/Fuyulin-hub/kanban/git/matching-refs/heads/board/` → exit 0
  - 0条记录
- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'C:\Users\ASUS\Documents\Codex\2026-11-03\new-chat\work\gh_publish_payload.json'` → exit 0
  - {"sha": "a32e4c4547e70a4d5b2e3a3c538754137a66deb5"}
- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'C:\Users\ASUS\Documents\Codex\2026-11-03\new-chat\work\gh_publish_payload.json'` → exit 0
  - {"sha": "dc934b5c37c736d0cefa20d6dc63f5ef0d5b7d49"}
- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'C:\Users\ASUS\Documents\Codex\2026-11-03\new-chat\work\gh_publish_payload.json'` → exit 0
  - {"sha": "1c56edd0be3969561ef1a9d9a2330398f23242e9"}
- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'C:\Users\ASUS\Documents\Codex\2026-11-03\new-chat\work\gh_publish_payload.json'` → exit 0
  - {"sha": "a5af88fdfb0492abab623077ff8aee24a57c7078"}
- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'C:\Users\ASUS\Documents\Codex\2026-11-03\new-chat\work\gh_publish_payload.json'` → exit 0
  - {"sha": "03bb8f098a6a34ea4f1a5b642a865dac0a063028"}
- `gh api --method POST repos/Fuyulin-hub/kanban/git/trees --input 'C:\Users\ASUS\Documents\Codex\2026-11-03\new-chat\work\gh_publish_payload.json'` → exit 0
  - {"sha": "8e8d7ba984960d8eaa63386e6de7681b2ffbe9da"}
- `gh api --method POST repos/Fuyulin-hub/kanban/git/commits --input 'C:\Users\ASUS\Documents\Codex\2026-11-03\new-chat\work\gh_publish_payload.json'` → exit 0
  - {"sha": "feb35bf897415fdcf6de991696c53941c2c5e874", "html_url": "https://github.com/Fuyulin-hub/kanban/commit/feb35bf897415fdcf6de991696c53941c2c5e874"}
- `gh api --method POST repos/Fuyulin-hub/kanban/git/refs --input 'C:\Users\ASUS\Documents\Codex\2026-11-03\new-chat\work\gh_publish_payload.json'` → exit 0
  - {"ref": "refs/heads/board/wechat-20261103-032234"}
- `gh pr create --repo Fuyulin-hub/kanban --base main --head board/wechat-20261103-032234 --title '群聊任务看板与判定依据' --body-file 'C:\Users\ASUS\Documents\Codex\2026-11-03\new-chat\work\native_pr_body.md'` → exit 0
  - https://github.com/Fuyulin-hub/kanban/pull/49
- `gh api 'repos/Fuyulin-hub/kanban/pulls/49/files?per_page=100'` → exit 0
  - 5条记录
- `gh api repos/Fuyulin-hub/kanban/git/ref/heads/main` → exit 0
  - {"ref": "refs/heads/main"}

实际PR：https://github.com/Fuyulin-hub/kanban/pull/49

读回验证：48个Issue；待确认36；assignee均为空；Status四列与本地CSV逐项一致；PR仅包含5个board文件；main仍为批准的README初始化提交。

最后一次清单与审计文件的回写提交，其SHA和成功结果保存在PR提交历史及PR描述中，避免审计文件自引用自身提交。


<!-- ENRICHMENT_AUDIT_START -->

## 2026-11-03：补充工作板块、四人身份与逐项建议

- 授权依据：用户要求继续添加板块、各任务的做法及库，并区分四人的工作；随后确认张馨月、徐佳乐、王思琦、付玉琳四人身份，明确允许使用四人完整姓名。手机号继续隐藏。

- 沿用已有官方gh OAuth登录，未使用或保存聊天中出现的PAT；没有改变GitHub assignee。

- 在48个原Issue末尾添加有独立标记的身份补充和建议；没有创建虚构的新任务或假冒成员发布评论。

- 分成7个工作板块，创建4个个人建议视图；新增工作板块、建议执行人、原文负责人、证据发言者4字段。全部新ID由API读取。

- 网络中途发生TLS握手和连接超时。每次失败后先读取项目现状，再只补尚缺字段/筛选设置；未重新创建Issue或重复追加方案。

- 一次多类型GraphQL introspection受服务端最多两次字段查询限制，后拆为小批只读查询；没有因此改变权限或身份。

- 原CSV继续作为初始群聊提取记录；execution_plans.json单独保存建议。import_board.py增加保留方案和成员后续备注的合并逻辑。

- 本地12项完整离线行为测试通过；随PR提供的3项专项回归测试通过，覆盖重导保留方案、损坏标记停止及新增标签保留。没有执行真实重导，避免改动现有状态。

- 首次文件提交ab7d2fb264642e2a04a0528de4b7a4b8bba81d21已成功；其后CSV逐字节比对因原远端LF与本地BOM/CRLF格式差异停止。核对48行数据内容一致，未改动CSV；最终以原远端CSV blob SHA未变化作为验收。


### 原生项目读回结果


- 48个Issue、48个Project项；每项有且只有1段方案；原Issue标题、前缀证据、state和assignee保持。

- Status：Todo 6 / In Progress 2 / Done 4 / 待确认36。原始事实已完成4 / 未完成44；needs-review36是交叉维度。

- 48项×4个自定义字段逐项核对；11个新增视图均为原生BOARD_LAYOUT并按Status分列，标签筛选值已读回。

- 48项均有具体步骤、工具、建议牵头、协作、交付物、验收标准、前置条件和讨论题。

- 未重跑实验、修改报告或原始截图、部署站点、发送邮件或提交课程作业。


### 结构和任务更新日志


- 创建字段 工作板块 PVTSSF_lAHOC3MSJ84Bp7xgzhoVSnY

- 创建字段 建议执行人 PVTSSF_lAHOC3MSJ84Bp7xgzhoVSnc

- 创建字段 原文负责人 PVTF_lAHOC3MSJ84Bp7xgzhoVSng

- 创建字段 证据发言者 PVTF_lAHOC3MSJ84Bp7xgzhoVSnk

- 创建标签 module:资料与需求核对

- 创建标签 module:报告正文与翻译

- 创建标签 module:数据图表与实验

- 创建标签 module:文档排版与编译

- 创建标签 module:PPT与答辩

- 创建标签 module:网页与部署

- 创建标签 module:提交与交付

- 创建标签 建议执行人:张馨月

- 创建标签 建议执行人:徐佳乐

- 创建标签 建议执行人:王思琦

- 创建标签 建议执行人:付玉琳

- updateIssue batch 1—6: m0,m1,m2,m3,m4,m5 成功

- updateIssue batch 7—12: m0,m1,m2,m3,m4,m5 成功

- updateIssue batch 13—18: m0,m1,m2,m3,m4,m5 成功

- updateIssue batch 19—24: m0,m1,m2,m3,m4,m5 成功

- updateIssue batch 25—30: m0,m1,m2,m3,m4,m5 成功

- updateIssue batch 31—36: m0,m1,m2,m3,m4,m5 成功

- updateIssue batch 37—42: m0,m1,m2,m3,m4,m5 成功

- updateIssue batch 43—48: m0,m1,m2,m3,m4,m5 成功

- 48项Issue方案就绪，本次更新48项；未设置assignee或修改状态

- updateProjectV2ItemFieldValue batch 1—6: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 7—12: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 13—18: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 19—24: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 25—30: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 31—36: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 37—42: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 43—48: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 49—54: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 55—60: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 61—66: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 67—72: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 73—78: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 79—84: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 85—90: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 91—96: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 97—102: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 103—108: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 109—114: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 115—120: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 121—126: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 127—132: m0,m1,m2,m3,m4,m5 成功

- updateIssue batch 1—1: m0 成功

- 48项Issue方案就绪，本次更新1项；未设置assignee或修改状态

- updateProjectV2ItemFieldValue batch 1—6: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 7—12: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 13—18: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 19—24: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 25—30: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 31—36: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 37—42: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 43—48: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 49—54: m0,m1,m2,m3,m4,m5 成功

- updateProjectV2ItemFieldValue batch 55—60: m0,m1,m2,m3,m4,m5 成功

- 创建视图 资料与需求核对 #3

- 设置视图筛选 资料与需求核对 label:"module:资料与需求核对"

- 创建视图 报告正文与翻译 #4

- 设置视图筛选 报告正文与翻译 label:"module:报告正文与翻译"

- 创建视图 数据图表与实验 #5

- 设置视图筛选 数据图表与实验 label:"module:数据图表与实验"

- 创建视图 文档排版与编译 #6

- 设置视图筛选 文档排版与编译 label:"module:文档排版与编译"

- 创建视图 PPT与答辩 #7

- 设置视图筛选 PPT与答辩 label:"module:PPT与答辩"

- 创建视图 网页与部署 #8

- 设置视图筛选 网页与部署 label:"module:网页与部署"

- 创建视图 提交与交付 #9

- 设置视图筛选 提交与交付 label:"module:提交与交付"

- 创建视图 张馨月的建议任务 #10

- 设置视图筛选 张馨月的建议任务 label:"建议执行人:张馨月"

- 创建视图 徐佳乐的建议任务 #11

- 48项Issue方案就绪，本次更新0项；未设置assignee或修改状态

- 设置视图筛选 徐佳乐的建议任务 label:"建议执行人:徐佳乐"

- 创建视图 王思琦的建议任务 #12

- 设置视图筛选 王思琦的建议任务 label:"建议执行人:王思琦"

- 创建视图 付玉琳的建议任务 #13

- 设置视图筛选 付玉琳的建议任务 label:"建议执行人:付玉琳"

- 总视图显示新增成员与板块字段 View 1

- 总视图显示新增成员与板块字段 群聊任务看板

- 读回核对通过：48项、4字段、11新增视图，原证据/状态/assignee保持，列数{"待确认": 36, "In Progress": 2, "Done": 4, "Todo": 6}


### gh命令结果


以下逐条记录本次gh调用的退出结果；--input是本地结构化请求文件，日志只记录操作类型，不复制完整聊天或凭据。

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 1；gh: Introspection fields may only be used 2 times, but some fields were used more than that: __Type.inputFields (5) / 

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api 'repos/Fuyulin-hub/kanban/labels?per_page=100'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/labels --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 1；Post "https://api.github.com/graphql": net/http: TLS handshake timeout / 

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api 'repos/Fuyulin-hub/kanban/labels?per_page=100'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 1；Post "https://api.github.com/graphql": dial tcp 20.205.243.168:443: i/o timeout / 

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api 'repos/Fuyulin-hub/kanban/labels?per_page=100'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST graphql --input 'work\enrichment_payload.json'` → exit 0

- `gh api repos/Fuyulin-hub/kanban/pulls/49` → exit 0

- `gh api repos/Fuyulin-hub/kanban/git/ref/heads/main` → exit 0

- `gh api repos/Fuyulin-hub/kanban/git/ref/heads/board/wechat-20261103-032234` → exit 0

- `gh api repos/Fuyulin-hub/kanban/git/commits/fbd46cf53505dcd0319f3ad00211981ebce8bc81` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/blobs --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/trees --input 'work\enrichment_payload.json'` → exit 0

- `gh api --method POST repos/Fuyulin-hub/kanban/git/commits --input 'work\enrichment_payload.json'` → exit 0

- `gh api repos/Fuyulin-hub/kanban/git/ref/heads/board/wechat-20261103-032234` → exit 0

- `gh api --method PATCH repos/Fuyulin-hub/kanban/git/refs/heads/board/wechat-20261103-032234 --input 'work\enrichment_payload.json'` → exit 0

- `gh api 'repos/Fuyulin-hub/kanban/git/trees/20878bf59f69e612343df3acb15c5d2863abb578?recursive=1'` → exit 0

- `gh api 'repos/Fuyulin-hub/kanban/contents/board/issues.csv?ref=board/wechat-20261103-032234'` → exit 0

- `gh api repos/Fuyulin-hub/kanban/pulls/49` → exit 0

- `gh api repos/Fuyulin-hub/kanban/git/commits/ab7d2fb264642e2a04a0528de4b7a4b8bba81d21` → exit 0

- `gh api 'repos/Fuyulin-hub/kanban/contents/board/issues.csv?ref=board/wechat-20261103-032234'` → exit 0

- `gh api repos/Fuyulin-hub/kanban/pulls/49` → exit 0

- `gh api repos/Fuyulin-hub/kanban/git/ref/heads/main` → exit 0


### 文档提交方式


- 更新现有PR #49的功能分支board/wechat-20261103-032234；不再次初始化main、不合并PR。

- 通过同一gh登录态调用Git数据API写入board文件，创建新tree和commit，以force=false更新功能分支。每次更新前核对branch head，保留base tree上的其他文件。

- 提交后将核对PR文件范围、远端内容哈希与main未变化；提交SHA及读回结果存入PR描述和本地交付回执，避免审计文件自引用。
