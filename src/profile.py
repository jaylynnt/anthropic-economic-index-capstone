from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path("data")
FIGURE_DIR = Path("figures")
FIGURE_DIR.mkdir(exist_ok=True)

claude_file = DATA_DIR / "aei_claude_ai_2026-06-26.csv"
api_file = DATA_DIR / "aei_1p_api_2026-06-26.csv"

claude = pd.read_csv(claude_file)
api = pd.read_csv(api_file)

# 1. Automation Percentage Distribution:
claude_auto = claude[
    claude["metric_id"] == "collaboration_bucket_automation_pct"
]["value"]

api_auto = api[
    api["metric_id"] == "collaboration_bucket_automation_pct"
]["value"]

plt.figure(figsize=(8, 5))
plt.hist(claude_auto, bins=20, alpha=0.6, label="Claude.ai")
plt.hist(api_auto, bins=20, alpha=0.6, label="API")
plt.xlabel("Automation Percentage")
plt.ylabel("Number of Rows")
plt.title("Distribution of Automation Percentages")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURE_DIR / "automation_distribution.png")
plt.close()


# 2. Augmentation Percentage Distribution:
claude_aug = claude[
    claude["metric_id"] == "collaboration_bucket_augmentation_pct"
]["value"]

api_aug = api[
    api["metric_id"] == "collaboration_bucket_augmentation_pct"
]["value"]

plt.figure(figsize=(8, 5))
plt.hist(claude_aug, bins=20, alpha=0.6, label="Claude.ai")
plt.hist(api_aug, bins=20, alpha=0.6, label="API")
plt.xlabel("Augmentation Percentage")
plt.ylabel("Number of Rows")
plt.title("Distribution of Augmentation Percentages")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURE_DIR / "augmentation_distribution.png")
plt.close()


# 3. Mean Automation vs Augmentation:
summary = pd.DataFrame({
    "Source": ["Claude.ai", "API"],
    "Automation": [
        claude_auto.mean(),
        api_auto.mean()
    ],
    "Augmentation": [
        claude_aug.mean(),
        api_aug.mean()
    ]
})

summary_plot = summary.set_index("Source")

summary_plot.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.ylabel("Mean Percentage")
plt.title("Average Automation vs Augmentation")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(FIGURE_DIR / "automation_vs_augmentation.png")
plt.close()


# Print Summary:

print("\nSummary Statistics:")
print(summary)

print("\nClaude.ai Automation:")
print(claude_auto.describe())

print("\nAPI Automation:")
print(api_auto.describe())

print("\nClaude.ai Augmentation:")
print(claude_aug.describe())

print("\nAPI Augmentation:")
print(api_aug.describe())