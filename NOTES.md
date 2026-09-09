# Capstone Notes

## Source: 
https://huggingface.co/datasets/Anthropic/EconomicIndex/tree/main/release_2026_06_26

## Sources I read: 
- Anthropic Economic Index original research paper (2025)
- release_2026_06_26/data_documentation.md
- https://www.anthropic.com/news/anthropic-economic-index-insights-from-claude-sonnet-3-7
- Anthropic Economic Index Report: Cadences (June 26, 2026): https://www.anthropic.com/research/economic-index-june-2026-report

## Release + Version:
June 26, 2026
`release_2026_06_26`

## Download Date:
September 5, 2026

## License:
- Data released under CC-BY
- Code released under MIT License

## Citation:
Massenkoff, Maxim, Eva Lyubich, Szymon Sacher, Zoe Hitzig, Shaoyi Zhang, Ryan Heller, and Peter McCrory.  
"Anthropic Economic Index report: Cadences." June 26, 2026.  
https://www.anthropic.com/research/economic-index-june-2026-report

## How the Data was Collected:
Anthropic collected anonymized Claude.ai Free and Pro conversations and analyzed them using Clio, a privacy-preserving analysis tool that is designed to recognize patterns in large sets of conversations. The conversations used in this paper were collected between December 2024 and January 2025. Clio was used to classify the conversations according to occupational tasks, skills, and interaction patterns. Each conversation was analyzed and mapped to the most relevant task category in the U.S. Department of Labor's O*NET database.

For the June 2026 documentation, the release contains aggregated Claude usage metrics for April and May 2026. It provides separate files for Claude.ai usage and Anthropic first-party API usage.

## Unit of Observation:
In the paper, the unit of analysis is a Claude.ai conversation. For each conversation, it was analyzed individually and associated with its most relevant category in the O*NET database based on the type of work performed. Instead of containing the original conversations, the dataset contains conversation-level classifications that are aggregated into summarized task and occupation usage statistics. 

In the June 2026 release, the documentation states that each row represents one metric value for a specific combination of geography and analysis category. 

## How Labels Were Produced:
The original paper used automated classification to map Claude conversations to economic tasks and occupations. The system also categorized the type of interaction between the user and Claude as either augmentation or automation.

The June 2026 release expanded the published classifications and metrics. The documentation includes measurements related to usage percentages, multitasking status, AI autonomy, estimated education requirements, collaboration patterns, and artifact types.

## Verification Targets:
1. Roughly 36% of occupations showed AI use for at least 25% of their associated tasks.
2. The study analyzed over 4 million Claude conversations across its analyses.
3. Approximately 57% of interactions were augmentation, compared to 43% as automation.


## Dataset Inventory:
There were no missing values and both files contained the same 10 columnns.

The inventory script in `src/inventory.py` examined the two June 2026 CSV files.
- `aei_1p_api_2026-06-26.csv`: 73.70 MB, 491,705 rows, 10 columns
- `aei_claude_ai_2026-06-26.csv`: 209.02 MB, 1,636,573 rows, 10 columns

## Claimed vs. Actual:
1. The paper also reported that roughly 36% of occupations showed AI use in at least 25% of their associated tasks. This cannot be directly verified from the inventory alone and will require additional analysis of the occupation- and task-level metrics.
2. The paper stated that more than 4 million Claude conversations were analyzed. This number cannot be compared with the row counts in the June 2026 CSV files because the data is aggregated. Each row represents one metric value for a specific combination of geography and analysis category, rather than one individual conversation.
3. The paper also reported that approximately 57% of interactions were classified as augmentation and 43% as automation. These values were not calculated during the inventory step because the inventory focused on file structure, row counts, columns, data types, and missing values. 

Overall, the file structure and fields were consistent across both CSV files. The main difference between the original paper and the June 2026 release is that the paper discusses conversation-level analysis, while the June 2026 files contain aggregated metric rows.


## Raw Record Examples:
Claude.ai - 
1. Nepal: O*NET task
This row represents Claude.ai usage in Nepal for the ONET task “Recommend and provide advice on a wide variety of products and services.” The pct metric has a value of 1.75, meaning this task accounted for a small share of the relevant usage in that category. The fields appear consistent because the row is tied to a country, an ONET task, and a percentage metric.

2. Global: Task iteration
This row represents the global O*NET task “Recommend disposal of excess, defective, or obsolete stock.” The metric collaboration_task_iteration_pct has a value of 25.00, showing that 25% of the classified interactions for this task were associated with task iteration. This example shows that the dataset contains collaboration-style metrics in addition to general usage percentages.

3. Poland: SOC occupation
This row represents the occupation category “Building and Grounds Cleaning and Maintenance” in Poland. The metric artifact_explanation_or_answer_pct has a value of 9.52, meaning 9.52% of the relevant interactions were associated with an explanation-or-answer artifact type. This record is different from the O*NET task rows because it uses the soc_occupation category at hierarchy level 1.

4. Dominican Republic: AI autonomy
This row represents the O*NET category “Performing for or Working Directly with the Public” in the Dominican Republic. The metric ai_autonomy_mean has a value of 2.40, which is different from a percentage because it reports an average autonomy score rather than a share of usage. This shows that the value column has to be interpreted based on the metric_id.

API Examples:
5. Global: Estimated education requirement
This row represents an O*NET task involving assessing client functioning levels and areas of need. The metric human_education_years_mean has a value of 12.48, which appears to represent the estimated average years of human education associated with the task. This is another example where the value field is not a percentage.

6. Global: Automation
This row represents the O*NET task involving determining response requirements and dispatching units based on established procedures. The metric collaboration_bucket_automation_pct has a value of 100.00, meaning all classified interactions for this task in this slice were categorized as automation. This is an interesting record because it shows a task with a completely automation-heavy interaction pattern.

7. Global: Document or report artifact
This row represents the O*NET task about determining formats, approaches, content, levels, and mediums to meet objectives within budget constraints. The metric artifact_document_or_report_pct has a value of 3.80, meaning 3.8% of the relevant API usage for this task was associated with a document-or-report artifact. The row is global because the first-party API dataset is reported at the global geographic level in this example.