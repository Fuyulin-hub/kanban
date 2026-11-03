# Task execution playbook

These plans are proposals added for discussion. Source status, evidence and uncertainty remain in each issue. Completed tasks use review checklists and are not reopened.

## Requirements & References

### [T01: Obtain a previous-year reference report](https://github.com/Fuyulin-hub/kanban/issues/1)

Recorded status: Not started. Recorded owner: Unassigned (original alias unresolved).

Proposed lead: Wang Siqi. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Confirm whether the request was cancelled.
2. If still needed, request a copy from someone authorized to share it.
3. Record useful formatting examples without reusing their findings.

**Tools and libraries:** No additional library. Use a browser and PDF reader.

**Deliverable:** A reference list or a cancellation note.

**Acceptance:** Sources are traceable; previous-year data are never presented as this group's results.

**Discussion:** Is the reference still required, or was the request cancelled?

### [T06: Verify missingness in the real data](https://github.com/Fuyulin-hub/kanban/issues/6)

Recorded status: Not started. Recorded owner: Unassigned (original alias unresolved).

Proposed lead: Wang Siqi. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Identify the source version and unit of analysis for each table.
2. Count missing values and empty strings using applicable fields.
3. Report counts, denominators and rates and compare them with the text.

**Tools and libraries:** Use pandas for missingness and grouping; use merge(validate=...) when checking join cardinality.

**Deliverable:** A reproducible missingness table and script.

**Acceptance:** Separate raw and cleaned data; specify the table, field, population and denominator.

**Discussion:** The alias in the original assignment remains unresolved; the proposed lead is a new recommendation.

### [T16: Verify the official submission deadline](https://github.com/Fuyulin-hub/kanban/issues/16)

Recorded status: Not started. Recorded owner: Unassigned (original alias unresolved).

Proposed lead: Wang Siqi. Proposed collaborators: Fu Yulin.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Open the official course notice or assignment page.
2. Check date, timezone, channel and filename rules.
3. Record a traceable reference for the group.

**Tools and libraries:** Use the browser and course system; no additional library.

**Deliverable:** A submission-requirements checklist.

**Acceptance:** An uncertain chat statement about 23:59 is not an official deadline; do not reuse a prior-year notice.

**Discussion:** Where is the current official notice? The screenshot messages show no year.

### [T39: Verify how many members must submit the assignment](https://github.com/Fuyulin-hub/kanban/issues/39)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Wang Siqi. Proposed collaborators: Fu Yulin.

**Prerequisites:** Obtain the official requirements in T16.

**Steps**

1. Distinguish submission count from presentation attendance.
2. Check the formal assignment instructions.
3. If unclear, ask the instructor and record the reply.

**Tools and libraries:** Use the course page and browser; no additional library.

**Deliverable:** A checklist for submitter count, presenter count and required channels.

**Acceptance:** Uncertain chat statements or other groups' behavior are not official requirements.

**Discussion:** Is one representative submission sufficient, and is presenter count specified separately?

## Report & Translation

### [T02: Review the report content](https://github.com/Fuyulin-hub/kanban/issues/2)

Recorded status: In progress. Recorded owner: Unassigned.

Proposed lead: Zhang Xinyue. Proposed collaborators: Wang Siqi, Xu Jiale, Fu Yulin.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Agree on the file and chapters to review.
2. Check that questions, methods, data and conclusions match.
3. Locate each issue by page and sentence, then ask the relevant member to verify it.

**Tools and libraries:** Use the existing Word/WPS or TeX editor; Python difflib is optional for comparisons.

**Deliverable:** A page-specific review list and revision comparison.

**Acceptance:** Preserve meaning, numbers, subheadings and every figure/table.

**Discussion:** Does the exclusion of Section 7.3 onward still apply? Who reviews each section?

### [T04: Revise the first three report chapters](https://github.com/Fuyulin-hub/kanban/issues/4)

Recorded status: In progress. Recorded owner: Zhang Xinyue.

Proposed lead: Zhang Xinyue. Proposed collaborators: Wang Siqi.

**Prerequisites:** Agree on the review scope in T02.

**Steps**

1. Resolve the difference between the first-three-chapters claim and the later first-chapter clarification.
2. Confirm the paragraphs in scope.
3. Make subjects, objects and logical links explicit without changing meaning.

**Tools and libraries:** Keep the existing Word/WPS or TeX workflow; no new library is required.

**Deliverable:** A paragraph-level revision record for the agreed chapters.

**Acceptance:** Preserve the original meaning, subheadings, numbers and all figures/tables.

**Discussion:** Is this a Chapter 1 revision or a review of Chapters 1–3?

### [T08: Clarify the report wording about missing data](https://github.com/Fuyulin-hub/kanban/issues/8)

Recorded status: Not started. Recorded owner: Zhang Xinyue.

Proposed lead: Zhang Xinyue. Proposed collaborators: Wang Siqi.

**Prerequisites:** Verify the statistical definitions in T06 first.

**Steps**

1. Locate vague statements about excessive missing data.
2. Specify which field is missing and what analysis is affected.
3. Use the verified rate and denominator while retaining the limitation.

**Tools and libraries:** Use the existing editor; obtain numbers from the pandas checks in T06.

**Deliverable:** An original-versus-revised wording comparison.

**Acceptance:** Do not describe absent comments as corrupted orders or remove a real limitation.

**Discussion:** Does missingness mean no review body despite a rating, or a missing order?

### [T14: Integrate the report chapters](https://github.com/Fuyulin-hub/kanban/issues/14)

Recorded status: In progress. Recorded owner: Zhang Xinyue.

Proposed lead: Zhang Xinyue. Proposed collaborators: Wang Siqi, Xu Jiale.

**Prerequisites:** Complete the relevant chapter reviews in T02/T04 first.

**Steps**

1. Freeze the chapter input versions.
2. Unify terminology, figure numbers and cross-references.
3. Check for missing or repeated sections and record the merge.

**Tools and libraries:** Use the current Word/WPS/TeX editor; hashlib is optional for version checks.

**Deliverable:** An integrated report and chapter merge record.

**Acceptance:** Keep all subheadings and figures; do not mix numbers from different versions.

**Discussion:** Which file is the single editing master?

### [T18: Add Chapter 7 to the report](https://github.com/Fuyulin-hub/kanban/issues/18)

Recorded status: Completed. Recorded owner: Zhang Xinyue.

Proposed lead: Zhang Xinyue. Proposed collaborators: Xu Jiale.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Review the existing implementation plan and deliverables.
2. Check that its figures match the text.
3. Record the scope of any later additions.

**Tools and libraries:** Use the existing editor; no additional library.

**Deliverable:** A review record for the completed Chapter 7 addition.

**Acceptance:** Keep the completed status; adding a chapter does not complete its later charts or formatting.

**Discussion:** Does the current Chapter 7 match the schedule in T12?

### [T21: Review and clarify AI-style wording](https://github.com/Fuyulin-hub/kanban/issues/21)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Wang Siqi. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Use the master draft and content issues from T02/T14.

**Steps**

1. Mark abstract language, ambiguous references and long sentences.
2. Make subjects, objects and reasoning explicit.
3. Compare meaning before/after and ask another member to review.

**Tools and libraries:** Use tracked changes or a TeX diff; difflib is optional. No AI-detector score is needed.

**Deliverable:** A wording revision comparison.

**Acceptance:** Keep meaning, numbers, subheadings, figures/tables and the original level of uncertainty.

**Discussion:** Which sentences still take more than one reading to understand?

### [T23: Translate the report using the course terminology](https://github.com/Fuyulin-hub/kanban/issues/23)

Recorded status: In progress. Recorded owner: Unassigned.

Proposed lead: Wang Siqi. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Stabilize the wording reviewed in T21 first.

**Steps**

1. Build a bilingual glossary from the course materials.
2. Translate paragraph by paragraph and compare with the source.
3. Check numbers, negation, method names and limitations.

**Tools and libraries:** Use the current Word/WPS/TeX editor; re can help check numbers and terminology.

**Deliverable:** An English master draft, glossary and uncertainty list.

**Acceptance:** Preserve claim strength and use consistent terms such as low rating; explain retained Portuguese words.

**Discussion:** Do the course terms conflict with terminology already used in the project?

### [T37: Review the English report and source before formatting](https://github.com/Fuyulin-hub/kanban/issues/37)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Zhang Xinyue. Proposed collaborators: Wang Siqi, Xu Jiale.

**Prerequisites:** Use the English draft and source from T23/T35.

**Steps**

1. Match the PDF and source versions.
2. Check terms, figure numbers, sample counts and limitations.
3. Resolve content problems before handing over for formatting.

**Tools and libraries:** Use the existing editor and PDF reader; PyMuPDF/difflib can help locate changes.

**Deliverable:** A review checklist and handover record.

**Acceptance:** Keep content and layout review distinct and list unresolved items.

**Discussion:** Which English ambiguities require checking the original draft?

## Data & Figures

### [T03: Plan and refine the report figures](https://github.com/Fuyulin-hub/kanban/issues/3)

Recorded status: In progress. Recorded owner: Zhang Xinyue.

Proposed lead: Zhang Xinyue. Proposed collaborators: Xu Jiale.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. List the finding each research question needs to show.
2. Check existing figures before proposing additions.
3. Specify the result file, chart type and insertion point for each gap.

**Tools and libraries:** A spreadsheet is sufficient for the inventory; use Matplotlib when an existing Weka result needs plotting.

**Deliverable:** A figure inventory with purpose, source, location and proposed producer.

**Acceptance:** Each figure answers a clear question and uses the same result version.

**Discussion:** Which figures have editable source files and which need redrawing?

### [T05: Mark figure insertion points in the report](https://github.com/Fuyulin-hub/kanban/issues/5)

Recorded status: Completed. Recorded owner: Zhang Xinyue.

Proposed lead: Zhang Xinyue. Proposed collaborators: Xu Jiale.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Check the existing marks against current chapter numbers.
2. Verify that surrounding text refers to the correct figure.
3. Check the links again after pagination changes.

**Tools and libraries:** Use native cross-references; PyMuPDF is optional for PDF page checks.

**Deliverable:** A figure-to-paragraph/page index for this completed task.

**Acceptance:** Keep the completed status; every mark points to the intended figure.

**Discussion:** Have later additions changed the figure numbering?

### [T07: Add relevant illustrations to the first three chapters](https://github.com/Fuyulin-hub/kanban/issues/7)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Xu Jiale. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Use the figure gaps identified in T03.

**Steps**

1. Review the figures already present.
2. Identify a real explanatory gap in each section.
3. Prefer an editable workflow or data-relationship diagram and ask the content lead to check it.

**Tools and libraries:** Use PowerPoint shapes; Graphviz is optional if an editable diagram source already exists.

**Deliverable:** Candidate explanatory diagrams and editable sources.

**Acceptance:** Keep existing figures and distinguish conceptual diagrams from empirical results.

**Discussion:** Would a research workflow or a data-source diagram explain the text better?

### [T12: Draw the Chapter 7 implementation Gantt chart](https://github.com/Fuyulin-hub/kanban/issues/12)

Recorded status: Not started. Recorded owner: Unassigned (original alias unresolved).

Proposed lead: Xu Jiale. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Split the plan into verifiable stages.
2. Confirm dependencies and dates with the group.
3. Plot the stages on one timeline and leave unknown dates pending.

**Tools and libraries:** Use Matplotlib barh or editable PowerPoint shapes.

**Deliverable:** A Chapter 7 Gantt chart and stage table.

**Acceptance:** The stages match the text; no dates are invented.

**Discussion:** The original assigned alias is unresolved. Should Xu Jiale take this task?

### [T17: Improve the discussed fishbone diagram](https://github.com/Fuyulin-hub/kanban/issues/17)

Recorded status: Not started. Recorded owner: Zhang Xinyue.

Proposed lead: Xu Jiale. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Retain all concepts from the original diagram.
2. Align related branches and simplify labels.
3. Check the revised diagram against Chapter 4.

**Tools and libraries:** Use editable PowerPoint shapes or the existing Graphviz source.

**Deliverable:** An improved fishbone diagram and editable source.

**Acceptance:** Do not present hypothesized factors as established causes.

**Discussion:** Is this the same figure as T27? If so, share one source while retaining both task records.

### [T22: Identify and add missing report figures](https://github.com/Fuyulin-hub/kanban/issues/22)

Recorded status: Not started. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Confirm the figure inventory in T03.

**Steps**

1. Compare each section's question with the existing figures.
2. List only missing evidence or explanations.
3. Specify the input, purpose and location before making each addition.

**Tools and libraries:** Use a figure inventory; Matplotlib for data charts and PowerPoint for conceptual diagrams.

**Deliverable:** An approved additions list and the resulting figures.

**Acceptance:** Retain all existing figures and provide a source for each addition.

**Discussion:** Which figures add necessary evidence and which only change the layout?

### [T26: Improve the risk-scoring workflow diagram](https://github.com/Fuyulin-hub/kanban/issues/26)

Recorded status: Not started. Recorded owner: Zhang Xinyue.

Proposed lead: Xu Jiale. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Verify the actual inputs, outputs and point in time.
2. Keep the meaning while aligning boxes and arrows.
3. Ask the content lead to check every node.

**Tools and libraries:** Use native PowerPoint shapes or optional Graphviz; no new ML library is needed.

**Deliverable:** An editable risk-scoring workflow diagram.

**Acceptance:** Match the actual method; do not use future review text as an input to an earlier prediction.

**Discussion:** Does the figure describe a proposal or an implemented workflow? Label it accordingly.

### [T27: Correct the fishbone diagram and move it to Chapter 4](https://github.com/Fuyulin-hub/kanban/issues/27)

Recorded status: Not started. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Share the source with T17 and confirm the Chapter 4 version.

**Steps**

1. Check every branch against Chapter 4.
2. Correct misplaced factors and placement.
3. Insert the diagram and update the text reference.

**Tools and libraries:** Use PowerPoint or the existing fishbone source; no additional library.

**Deliverable:** The corrected Chapter 4 figure and insertion reference.

**Acceptance:** Keep its conceptual scope; do not treat it as causal proof.

**Discussion:** If Chapter 7 already has a Gantt chart, should its fishbone diagram be omitted?

### [T28: Add two preprocessing diagrams to Chapter 4](https://github.com/Fuyulin-hub/kanban/issues/28)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Xu Jiale. Proposed collaborators: Wang Siqi, Zhang Xinyue.

**Prerequisites:** Obtain the actual preprocessing steps and checks in T06.

**Steps**

1. First confirm which two diagrams were intended.
2. If unspecified, propose a table-join workflow and a sample-filtering workflow.
3. Use the actual processing order and verified counts.

**Tools and libraries:** Use pandas to verify outputs; draw editable flows with PowerPoint or Graphviz.

**Deliverable:** A content confirmation note, two source diagrams and Chapter 4 locations.

**Acceptance:** The two topics are new proposals; do not estimate sample counts from images.

**Discussion:** The source does not name the two diagrams. What should they show?

### [T29: Visualize the order clusters](https://github.com/Fuyulin-hub/kanban/issues/29)

Recorded status: Not started. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Wang Siqi, Zhang Xinyue.

**Prerequisites:** Obtain the same-version Weka output and sample definition.

**Steps**

1. Read the saved cluster assignments and feature definitions.
2. Show cluster sizes and feature profiles.
3. If a PCA view is needed, identify it as a display projection only.

**Tools and libraries:** Reuse the existing Weka SimpleKMeans results; summarize with pandas and plot with Matplotlib.

**Deliverable:** An order-cluster figure, profile table and result reference.

**Acceptance:** Cluster sizes sum to the analysis population; do not infer causes from the projection.

**Discussion:** Are features, scaling and the random seed recorded?

### [T30: Visualize category co-purchases](https://github.com/Fuyulin-hub/kanban/issues/30)

Recorded status: Not started. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Wang Siqi, Zhang Xinyue.

**Prerequisites:** Obtain the real basket data and rule output.

**Steps**

1. Read the actual association-rule output.
2. Check co-purchase counts, support, confidence and lift separately.
3. Draw a readable bar chart and state multi-category-basket coverage.

**Tools and libraries:** Reuse the existing Weka association output; verify with pandas and plot with Matplotlib.

**Deliverable:** A co-purchase chart and rule-metric table.

**Acceptance:** State the support denominator; frequency is not lift; explain sparse multi-category coverage and weak associations.

**Discussion:** Which algorithm actually ran? Use the log rather than assuming Apriori.

### [T31: Visualize the Portuguese review analysis](https://github.com/Fuyulin-hub/kanban/issues/31)

Recorded status: Not started. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Wang Siqi, Zhang Xinyue.

**Prerequisites:** Confirm the actual model and grouping; do not automatically retrain.

**Steps**

1. Confirm the text-bearing review sample and rating groups.
2. Read the existing text-model output and select representative words.
3. Preserve the meaning of negation and explain sample limitations.

**Tools and libraries:** Reuse the saved Weka TF-IDF/Naive Bayes pipeline; confirm the exact filter/classifier from its configuration. Use pandas and Matplotlib.

**Deliverable:** A Portuguese word figure, sample description and result index.

**Acceptance:** Do not infer causes from word frequency or use post-review analysis as pre-review prediction.

**Discussion:** Does the figure show frequency, distinguishing words or model weights?

### [T38: Create the missingness visualization](https://github.com/Fuyulin-hub/kanban/issues/38)

Recorded status: Not started. Recorded owner: Zhang Xinyue.

Proposed lead: Xu Jiale. Proposed collaborators: Wang Siqi, Zhang Xinyue.

**Prerequisites:** Resolve T06 definitions and keep wording consistent with T08.

**Steps**

1. Read the verified missingness table.
2. Plot field-level missingness and show basket coverage separately.
3. Explain the practical effect beside each chart.

**Tools and libraries:** Use pandas for calculation and a Matplotlib horizontal bar chart; no extra charting framework.

**Deliverable:** Missingness and coverage figures with reproducible tables.

**Acceptance:** Different denominators remain separate; do not copy historical percentages into another report version.

**Discussion:** Does the current report use the same denominator as the earlier chat figures?

## Formatting & Compilation

### [T09: Complete the first report compilation](https://github.com/Fuyulin-hub/kanban/issues/9)

Recorded status: Completed. Recorded owner: Zhang Xinyue.

Proposed lead: Zhang Xinyue. Proposed collaborators: Wang Siqi.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Retain the record of the first successful build.
2. Open its output PDF in the existing environment.
3. Check fonts, figures and equations.

**Tools and libraries:** Use the actual TeX compiler; PyMuPDF is optional for page rendering.

**Deliverable:** An output/log index for this completed task.

**Acceptance:** A first successful build does not prove final pagination or contents are correct.

**Discussion:** Does the first build use the same source as the final English version?

### [T24: Improve the report formatting](https://github.com/Fuyulin-hub/kanban/issues/24)

Recorded status: In progress. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Wang Siqi, Zhang Xinyue.

**Prerequisites:** Use a stable integrated English draft from T14/T23.

**Steps**

1. Unify body text, headings, headers, footers and captions.
2. Fix large blank areas, floating figures and awkward page breaks.
3. Export and inspect every PDF page.

**Tools and libraries:** Keep the existing TeX or Word/WPS workflow; PyMuPDF is optional for rendering.

**Deliverable:** A formatted source, PDF and unresolved-issues list.

**Acceptance:** Do not remove content or figures to eliminate whitespace; check cover, contents and fonts.

**Discussion:** Should large blank areas or background consistency be fixed first?

### [T25: Reinsert the cover into the English report](https://github.com/Fuyulin-hub/kanban/issues/25)

Recorded status: Not started. Recorded owner: Zhang Xinyue.

Proposed lead: Zhang Xinyue. Proposed collaborators: Xu Jiale.

**Prerequisites:** Confirm the English title in T23.

**Steps**

1. Confirm the English title, course and group details.
2. Insert the selected cover asset.
3. Check proportions, resolution and page-number continuity.

**Tools and libraries:** Use the current editor's image tools; no additional library.

**Deliverable:** The source with its English cover and a first-page preview.

**Acceptance:** Use the four confirmed names; a shared cover image alone is not proof of insertion.

**Discussion:** Which cover version is approved for the final report?

### [T34: Fix the English table of contents](https://github.com/Fuyulin-hub/kanban/issues/34)

Recorded status: In progress. Recorded owner: Unassigned.

Proposed lead: Wang Siqi. Proposed collaborators: Xu Jiale.

**Prerequisites:** Use the English titles and complete source from T23/T35.

**Steps**

1. Establish whether the master source is TeX or Word.
2. Use the source's heading structure and automatic contents mechanism.
3. Check English titles, levels and page numbers.

**Tools and libraries:** For TeX use the actual compiler/latexmk; for Word/WPS use heading styles and refresh the contents.

**Deliverable:** A correct English contents page and reproducible instructions.

**Acceptance:** Every entry matches a heading; do not mix Word-generated and TeX-generated contents.

**Discussion:** Which output is the final submission master?

### [T35: Provide the English report LaTeX source](https://github.com/Fuyulin-hub/kanban/issues/35)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Wang Siqi. Proposed collaborators: Zhang Xinyue, Xu Jiale.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Collect the matching tex, figures, bibliography and required dependencies.
2. Identify the entry file and build command.
3. Verify that the source corresponds to the shared PDF.

**Tools and libraries:** Use pathlib, zipfile and hashlib if an automated inventory is useful; no third-party package is required.

**Deliverable:** A buildable source package and file inventory.

**Acceptance:** Do not omit figures or required dependencies; exclude chat files and credentials.

**Discussion:** Does the shared tex file have all its dependencies, and who has the full version?

### [T36: Recompile to resolve the table of contents](https://github.com/Fuyulin-hub/kanban/issues/36)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Wang Siqi. Proposed collaborators: Xu Jiale.

**Prerequisites:** Complete the contents configuration and source package in T34/T35.

**Steps**

1. Run the appropriate build command in the current environment.
2. Continue as required until contents and references stabilize.
3. Review warnings and PDF page numbers.

**Tools and libraries:** Use the existing MiKTeX/TeX Live setup and optional latexmk; follow warnings rather than assuming two passes always suffice.

**Deliverable:** A final PDF, build log and contents check record.

**Acceptance:** No unresolved references or missing figures; record enough environment details to reproduce the build.

**Discussion:** Are bibliography or cross-reference passes still needed?

### [T42: Shorten captions for the new figures](https://github.com/Fuyulin-hub/kanban/issues/42)

Recorded status: Not started. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Confirm the additions list in T22.

**Steps**

1. Identify the new captions rather than deleting notes globally.
2. Keep the explanation, sample, units and essential limitations.
3. Remove repetition and review each figure again.

**Tools and libraries:** Use the current editor; no additional library.

**Deliverable:** A caption comparison and revised PDF.

**Acceptance:** A reader can understand the figure and its denominator without losing essential limitations.

**Discussion:** Which two edits were referenced, and were all new captions covered?

### [T43: Remove the four indicated parenthetical passages](https://github.com/Fuyulin-hub/kanban/issues/43)

Recorded status: Not started. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Locate the four specific passages in the source image.
2. Distinguish explanatory notes from equations or citations.
3. Change only those four and check the resulting grammar.

**Tools and libraries:** Use tracked changes or the original TeX editor; do not globally remove parentheses.

**Deliverable:** A four-location before/after comparison.

**Acceptance:** Keep citations, formulas, intervals and unrelated parentheses intact.

**Discussion:** Which four locations were indicated, and do they still exist in the current version?

### [T44: Choose a report background that matches the cover](https://github.com/Fuyulin-hub/kanban/issues/44)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Xu Jiale. Proposed collaborators: Wang Siqi, Zhang Xinyue.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Review the shared candidates and permission to use them.
2. Compare pale teal/white or similarly light options.
3. Test them on a body-text page for contrast and distraction.

**Tools and libraries:** Use the existing editor's preview; no new library or generated image is required.

**Deliverable:** A candidate comparison and final selection record.

**Acceptance:** Do not obstruct text or treat a shared candidate as an adopted background.

**Discussion:** Who approves the final choice, and how should cover consistency balance readability?

### [T45: Test candidate backgrounds in the report](https://github.com/Fuyulin-hub/kanban/issues/45)

Recorded status: Not started. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Wang Siqi.

**Prerequisites:** Select candidates in T44 first.

**Steps**

1. Insert a candidate in a copy or background layer.
2. Test dense text, figure and contents pages.
3. Export and check the PDF for obstruction and file size.

**Tools and libraries:** Use Word/WPS page backgrounds or the existing TeX background mechanism.

**Deliverable:** A trial PDF and comparable sample pages.

**Acceptance:** Keep every original figure complete and preserve text readability.

**Discussion:** Would backgrounds on divider pages alone work better?

## Slides & Presentation

### [T10: Create the group presentation slides](https://github.com/Fuyulin-hub/kanban/issues/10)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Fu Yulin. Proposed collaborators: Zhang Xinyue, Xu Jiale.

**Prerequisites:** Use the reviewed report and figure inventory from T02/T03.

**Steps**

1. Structure the story around questions, methods, evidence and limitations.
2. Use verified text and figures from the report.
3. Give each slide one main point and add speaker notes.

**Tools and libraries:** Prefer PowerPoint/WPS; use python-pptx only for repetitive generation or checks.

**Deliverable:** An editable slide deck and exported PDF.

**Acceptance:** Numbers match the report and charts retain axes, legends and essential notes.

**Discussion:** What is the official time limit and which content must be shown?

### [T11: Explain the division of work in the slides](https://github.com/Fuyulin-hub/kanban/issues/11)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Fu Yulin. Proposed collaborators: Zhang Xinyue, Xu Jiale, Wang Siqi.

**Prerequisites:** Use members.md and ask all four members to review it.

**Steps**

1. Create a work-allocation slide using the four confirmed names.
2. Separate documented work from proposed next steps.
3. Ask each member to verify their entry before presenting it.

**Tools and libraries:** A PowerPoint/WPS table is sufficient; no additional library.

**Deliverable:** A verified contribution and next-step slide.

**Acceptance:** Do not present recommendations as completed work or infer GitHub accounts.

**Discussion:** Which follow-up tasks will each member actually accept?

### [T15: Refine and format the presentation slides](https://github.com/Fuyulin-hub/kanban/issues/15)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Fu Yulin. Proposed collaborators: Xu Jiale, Zhang Xinyue.

**Prerequisites:** Start after T10 has a complete draft.

**Steps**

1. Unify type sizes, fonts and colors.
2. Balance text density and chart size.
3. Check long titles and legends on the actual presentation device.

**Tools and libraries:** Use the PowerPoint/WPS master; python-pptx is optional for repetitive checks.

**Deliverable:** A formatted editable deck and playback check record.

**Acceptance:** Keep data visible and text readable at the projected aspect ratio.

**Discussion:** Who gives the final content, figure and speaker-note checks?

### [T20: Prepare the presentation script](https://github.com/Fuyulin-hub/kanban/issues/20)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Fu Yulin. Proposed collaborators: Zhang Xinyue, Xu Jiale, Wang Siqi.

**Prerequisites:** Stabilize the slide order in T10/T15 first.

**Steps**

1. Write natural spoken notes for each slide's main point.
2. Explain the data, method and limitations.
3. Rehearse with timing and clear handover sentences.

**Tools and libraries:** Use slide notes or a text document; no additional library.

**Deliverable:** A slide-by-slide script, timing record and handover plan.

**Acceptance:** Do not turn associations into causal claims; acknowledge unverified results.

**Discussion:** How many people will speak and which section will each cover?

### [T32: Adapt the figures to the slide layout](https://github.com/Fuyulin-hub/kanban/issues/32)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Fu Yulin. Proposed collaborators: Xu Jiale.

**Prerequisites:** Obtain complete figures from T29–T31.

**Steps**

1. Determine the available slide area.
2. Prefer re-exporting at a suitable aspect ratio or splitting across slides.
3. If cropping is necessary, retain axes, legends, titles and sample notes.

**Tools and libraries:** Prefer the original plotting tool or PowerPoint crop tools; no additional image library.

**Deliverable:** Slide-ready figures with references to the complete originals.

**Acceptance:** Do not crop data or limitations; labels must be readable in playback.

**Discussion:** Would splitting three figures across slides be clearer?

### [T46: Prepare evidence-based answers using the slides](https://github.com/Fuyulin-hub/kanban/issues/46)

Recorded status: Not started. Recorded owner: Xu Jiale.

Proposed lead: Xu Jiale. Proposed collaborators: Fu Yulin, Zhang Xinyue, Wang Siqi.

**Prerequisites:** Use the stable slides and review results from T10/T37.

**Steps**

1. List likely questions for each slide.
2. Link each answer to a report page, figure or experiment record.
3. Practice explaining the limits of unverified results.

**Tools and libraries:** Use the existing chat tool or a plain document; no API integration or Q&A system is required.

**Deliverable:** A question–answer–evidence index.

**Acceptance:** Generated answers are not evidence and must not create results.

**Discussion:** Which questions can be answered from evidence and which remain unverified?

### [T47: Add the dashboard link to the slides](https://github.com/Fuyulin-hub/kanban/issues/47)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Fu Yulin. Proposed collaborators: Wang Siqi.

**Prerequisites:** Confirm the site URL and deck version in T33/T15.

**Steps**

1. Insert the confirmed final URL on the appropriate slide.
2. Test it in slideshow mode.
3. Prepare offline screenshots or a backup demonstration.

**Tools and libraries:** Use PowerPoint/WPS hyperlinks and browser checks; no additional library.

**Deliverable:** A deck with a tested link and offline backup.

**Acceptance:** The URL targets the approved version and contains no local path; network availability remains a separate check.

**Discussion:** What will be shown if the venue has no usable network?

### [T48: Arrange and deliver the group presentation](https://github.com/Fuyulin-hub/kanban/issues/48)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Fu Yulin. Proposed collaborators: Zhang Xinyue, Xu Jiale, Wang Siqi.

**Prerequisites:** Resolve presenter count in T39 and prepare T20/T46/T47.

**Steps**

1. Confirm the presenter list against the formal requirements.
2. Assign opening, content, demonstration and handovers.
3. Rehearse with timing and check equipment, files and backups.

**Tools and libraries:** Use the slides, a timer and a checklist; no additional library.

**Deliverable:** A presenter list, segment allocation and demonstration checklist.

**Acceptance:** Do not assume all four must present; actual attendance/presentation evidence is needed for completion.

**Discussion:** What was the final arrangement after the messages about three presenters and an individual volunteer?

## Website & Deployment

### [T13: Design a dashboard prototype and share screenshots](https://github.com/Fuyulin-hub/kanban/issues/13)

Recorded status: Not started. Recorded owner: Unassigned (original alias unresolved).

Proposed lead: Wang Siqi. Proposed collaborators: Zhang Xinyue, Fu Yulin.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Confirm whether the page is a proposed interface or a display of existing results.
2. Reuse the current HTML structure.
3. Add questions, figures and limitations and capture desktop/mobile previews.

**Tools and libraries:** Use existing HTML/CSS/JavaScript; add Chart.js only if interactive charts are needed.

**Deliverable:** An accessible local prototype and preview screenshots.

**Acceptance:** Mark mock content clearly and use the report's result version; keep website deployment files out of this tracking repository.

**Discussion:** Confirm the original assignee and whether this is a prototype or a results page.

### [T19: Update the dashboard layout and colors](https://github.com/Fuyulin-hub/kanban/issues/19)

Recorded status: Completed. Recorded owner: Zhang Xinyue.

Proposed lead: Zhang Xinyue. Proposed collaborators: Wang Siqi, Fu Yulin.

**Prerequisites:** Confirm the current working version before starting.

**Steps**

1. Check the modified page against the report theme.
2. Verify text contrast and the meaning of chart colors.
3. Open it on both desktop and mobile.

**Tools and libraries:** Use the current HTML/CSS and browser tools; no frontend rebuild is required.

**Deliverable:** A review record for the completed page/color update.

**Acceptance:** Keep the completed status; a color change does not prove public deployment is complete.

**Discussion:** Which local or hosted version is the editing master?

### [T33: Publish the dashboard for external access](https://github.com/Fuyulin-hub/kanban/issues/33)

Recorded status: Not started. Recorded owner: Unassigned (original alias unresolved).

Proposed lead: Wang Siqi. Proposed collaborators: Fu Yulin, Zhang Xinyue.

**Prerequisites:** Confirm the page and English content versions in T13/T19/T23.

**Steps**

1. Confirm the source files and hosting account.
2. Use an existing approved hosting workflow with the correct entry file.
3. Check desktop, mobile and a signed-out browser and save the results.

**Tools and libraries:** Use the existing static HTML/CSS/JavaScript and confirmed hosting platform, such as the existing Cloudflare Pages setup.

**Deliverable:** A site URL, deployed-version reference and access-check record.

**Acceptance:** External access and resources work; posting a URL alone is not full acceptance.

**Discussion:** The original assigned alias is unresolved. Who controls the hosting account and source?

## Submission & Delivery

### [T40: Submit the Project Proposal by email](https://github.com/Fuyulin-hub/kanban/issues/40)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Wang Siqi. Proposed collaborators: Zhang Xinyue.

**Prerequisites:** Confirm T16/T39 and validate the final files in T36.

**Steps**

1. Verify the official email requirement and final package.
2. Confirm the actual sender and recipient.
3. After actual sending, record timestamp, attachment version and evidence.

**Tools and libraries:** Use the existing email client; zipfile/hashlib are optional for package checks.

**Deliverable:** A pre-send checklist; add submission evidence only after sending.

**Acceptance:** Do not mark complete before actual sending; this plan does not send email.

**Discussion:** Who sends it, who is copied, and what subject/filename is required?

### [T41: Confirm and follow the Moodle submission process](https://github.com/Fuyulin-hub/kanban/issues/41)

Recorded status: Not started. Recorded owner: Unassigned.

Proposed lead: Wang Siqi. Proposed collaborators: Fu Yulin.

**Prerequisites:** Resolve channels and submitter count in T16/T39.

**Steps**

1. Check whether Moodle is still required by the current official notice.
2. If required, verify the entry, package and confirmation screen.
3. Record the platform's success evidence after submitting.

**Tools and libraries:** Use the browser and Moodle; no additional library.

**Deliverable:** A channel decision and, if applicable, platform submission evidence.

**Acceptance:** A suggestion to use both channels is not an official dual-submission requirement.

**Discussion:** Does the later email instruction supersede Moodle or supplement it?
