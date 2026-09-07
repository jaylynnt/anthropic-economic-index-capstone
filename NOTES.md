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


