# Capstone Progress Log

## Week of September 5–9, 2026

### Progress
- Created the GitHub repository and required project structure.
- Selected the June 26, 2026 Anthropic Economic Index release.
- Downloaded the Claude.ai and first-party API datasets.
- Documented the dataset source, release, license, citation, collection methodology, and unit of observation in `NOTES.md`.
- Created `src/inventory.py` to examine file sizes, row counts, columns, data types, and missing values.
- Found 1,636,573 rows in the Claude.ai dataset and 491,705 rows in the API dataset.
- Examined sample records from both datasets using `src/sample_records.py`.
- Created `src/profile.py` to explore automation and augmentation usage.
- Created figures comparing automation and augmentation distributions between Claude.ai and API.
- Initial results showed that Claude.ai usage was relatively balanced between automation and augmentation, while API usage was substantially more automation-oriented.
- Documented the initial exploratory findings in `PROFILE.md`.

### Limitation Identified
- The initial analysis compares all available automation and augmentation metric rows and does not yet restrict the comparison to identical O*NET tasks between Claude.ai and API.

---

## Week of October 5, 2026

### Progress
- Reviewed the initial exploratory analysis and research question.
- Updated `PROFILE.md` to clearly present the dataset, figures, findings, current limitation, and next analysis step.
- Determined that the next analysis should make an apples-to-apples comparison by matching identical O*NET tasks between Claude.ai and API.

### In Progress
- Developing the matched O*NET task analysis.

### Next Steps
- Identify O*NET tasks shared by both datasets.
- Compare automation percentages for identical tasks.
- Calculate the automation gap between API and Claude.ai.
- Determine whether the initial difference remains after accounting for differences in task composition.