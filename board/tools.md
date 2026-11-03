# 工具与库使用建议

以下是本次执行方案的技术建议，没有安装这些依赖、重跑实验或改动现有报告/网页。优先沿用已有环境和实际模型，只在明确需要时加库；不要求为每条任务编程。官方资料核对日期：2026-11-03。

| 场景 | 建议工具或库 | 具体用途与选择条件 |
| --- | --- | --- |
| 缺失率、联表与指标核对 | pandas | 统计空值、分组与分母；联表时核对键和基数。先固定原始表/订单/篮子/评论的统计单位。[官方merge文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) |
| 数据图与甘特图 | Matplotlib | 从实际结果表生成数据图；barh可绘横向条形及计划条。无需为了排版重训模型。[官方barh文档](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html) |
| 现有数据挖掘 | Weka | 优先沿用已有聚类、关联规则和文本分析流程及日志，具体算法与参数以项目实际记录为准。[Weka官方资料](https://waikato.github.io/weka-wiki/) |
| 流程图、鱼骨图 | PowerPoint原生形状；已有Graphviz源则沿用 | 保留可编辑文字、分支与箭头。属于概念示意，不新增实验结果；无需另装复杂图形框架。 |
| 正文表达与翻译 | 原Word/WPS/TeX编辑器；Python标准库difflib、re可选 | 人工逐句核对含义；必要时定位文本差异和术语。无需AI检测工具评分作为“改清楚”的证明。 |
| PDF检查 | PDF阅读器；需要批量渲染时用PyMuPDF | 检查丢图、字体、页码、遮挡与跨页。渲染后的人工复核不能省略。[官方教程](https://pymupdf.readthedocs.io/en/latest/tutorial.html) |
| 英文目录与编译 | 原TeX引擎、latexmk或原Word/WPS目录功能 | 不混用源码链路；按编译警告运行到目录和引用稳定，不认为固定两次必定成功。 |
| PPT | PowerPoint/WPS；批量处理时才选python-pptx | 保留现有母版和可编辑图；导出后实际播放检查。python-pptx仅为可选批处理工具。[官方文档](https://python-pptx.readthedocs.io/en/latest/) |
| 可视化网页 | 现有HTML/CSS/JavaScript；交互图需要时选Chart.js | 沿用静态页面；只有需要交互时增加图表库，不默认迁移到React或增加后端。[Chart.js官方文档](https://www.chartjs.org/docs/latest/) |
| 打包与版本清单 | Python标准库pathlib、zipfile、hashlib，或系统压缩功能 | 记录最终文件版本、包内清单和校验值；无须安装第三方打包库。 |
| 提交与试讲 | 浏览器、邮箱/Moodle、计时器 | 先核对正式要求；本次没有代发邮件、代交作业或对外重新部署站点。无需SMTP/API自动化。 |

## 选择和验收原则

- 先复用当前项目实际结果与工具，不把推荐库写成小组已经使用过的库。若无法取得现有配置，先登记缺口。
- 图中每个数值应能追溯到同版本结果。截图里的历史比例不能覆盖另一阶段报告的统计结果。
- Support、confidence、lift和共购次数分别核对；评论缺失率与多品类篮子覆盖率的分母分别说明。
- 聚类PCA投影只解释二维展示；鱼骨图只是待检验因素框架；风险图应说明使用时点。
- 正文修改以意思不变、读者一遍能理解为目标，保留小标题和全部图表。

## 看板维护

板块与个人视图使用Issue标签筛选，个人标签名为“建议执行人:姓名”，不是GitHub assignee。GitHub官方支持按标签和项目字段过滤并保存视图，见[官方说明](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects)。

每个Issue新增方案放在`execution-plan:start/end`标记之间。更新后的import_board.py重导原始CSV时保留这段及其后的成员备注；标签中非原始状态标签也保留。人工确认条目仍按原保护规则跳过。execution_plans.json是本次建议快照，不会自动覆盖成员后来修改的方案，也不会代替原始issues.csv的证据记录。

工作板块、自定义字段和11个新增视图是本次已建立的项目结构；原CSV导入脚本只维护原始任务与状态，不会在另一个新项目自动重建这些新增视图。当前项目上的新增字段和视图不会因重导而删除。后续新增任务需补相同板块与建议字段后才会进入对应筛选视图。
