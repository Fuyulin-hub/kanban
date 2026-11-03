# Tools and libraries

Use the existing project environment and actual saved results. These are recommendations; no packages were installed and no experiments were rerun. A noncoding task can explicitly require no additional library.

| Task type | Suggested tools | Purpose |
| --- | --- | --- |
| Missingness, joins, metric checks | pandas | Check counts, denominators and join cardinality. [Official merge documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html). |
| Data charts and Gantt charts | Matplotlib | Plot actual result tables; do not retrain a model for appearance. [Official barh documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html). |
| Existing data-mining workflows | Weka | Reuse saved clustering, association and text-analysis outputs; confirm the actual algorithms and settings. [Official resources](https://waikato.github.io/weka-wiki/). |
| Workflow/fishbone diagrams | PowerPoint shapes; existing Graphviz source if available | Keep text, branches and arrows editable; distinguish hypotheses from proven causes. |
| Writing and translation | Existing Word/WPS/TeX editor; optional difflib/re | Review meaning manually; compare changes and check terminology/numbers when useful. |
| PDF checks | PDF reader; optional PyMuPDF | Inspect fonts, figures, page numbers, clipping and page breaks. [Official tutorial](https://pymupdf.readthedocs.io/en/latest/tutorial.html). |
| Contents and compilation | Actual TeX compiler/latexmk or native Word/WPS contents tools | Follow the real build chain and repeat until references stabilize. |
| Slides | PowerPoint/WPS; optional python-pptx for repetitive work | Keep the editable master and check playback. [Official python-pptx documentation](https://python-pptx.readthedocs.io/en/latest/). |
| Website | Existing HTML/CSS/JavaScript; optional Chart.js | Add a charting library only when interaction is useful; do not assume a frontend migration. [Official Chart.js documentation](https://www.chartjs.org/docs/latest/). |
| Packages and version inventory | pathlib, zipfile, hashlib or system archive tools | Record files, versions and checksums without a new third-party dependency. |
| Submission and rehearsal | Browser, existing email/Moodle client, timer | Verify requirements and capture actual completion evidence; no email automation is needed. |

## Interpretation and validation

- Reuse the report's actual data version. Distinguish orders, baskets, reviews and text-bearing reviews as separate denominators.
- Check support, confidence, lift and raw co-purchase counts separately. Missing review bodies and multi-category-basket coverage are different quantities.
- Treat PCA as a display projection, fishbone branches as hypotheses, and risk inputs according to when they are available.
- Preserve meaning, subheadings and every existing figure/table when changing report wording.
- Proposed leads remain separate from GitHub assignees. Workstream and personal views use English label filters. [GitHub filtering documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects).

## Maintenance

The importer retains the marked execution-plan block and later member notes when source-only CSV records are reimported. It also preserves labels outside the managed source/status set and skips manually confirmed issues. A damaged plan marker stops the update rather than discarding content.

The existing project's extra fields and views survive reimport. The CSV importer does not recreate these custom views or all execution plans in another project; use the structured plans to maintain them separately. Changes to proposed plans should be reviewed before replacing a member-edited version.
