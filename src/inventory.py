from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")


def summarize_csv(file_path):
    df = pd.read_csv(file_path)

    print("=" * 80)
    print(f"File: {file_path.name}")
    print(f"Size (MB): {file_path.stat().st_size / (1024 ** 2):.2f}")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print()

    print("Column Types:")
    print(df.dtypes)
    print()

    print("Missing-Value Rates:")
    missing_rates = df.isna().mean().sort_values(ascending=False)
    print(missing_rates)
    print()


def main():
    csv_files = sorted(DATA_DIR.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in the data/ folder.")
        return

    for file_path in csv_files:
        summarize_csv(file_path)


if __name__ == "__main__":
    main()