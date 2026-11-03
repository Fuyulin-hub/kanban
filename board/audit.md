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
