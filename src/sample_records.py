import pandas as pd

claude_file = "data/aei_claude_ai_2026-06-26.csv"
api_file = "data/aei_1p_api_2026-06-26.csv"

claude_df = pd.read_csv(claude_file)
api_df = pd.read_csv(api_file)

print("\nClaude.Ai Sample Rows:\n")
print(claude_df.sample(5, random_state=42).to_string(index=False))

print("\nAPI Sample Rows:\n")
print(api_df.sample(5, random_state=42).to_string(index=False))