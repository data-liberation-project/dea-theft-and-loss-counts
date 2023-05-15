from pathlib import Path

import pandas as pd


def process(df: pd.DataFrame) -> None:
    for col in ["count", "unit", "gram", "milligram", "milliliter"]:
        if col in df.columns:
            print(f"{col}: {df[col].sum()}")


def main() -> None:
    paths = sorted(Path("data/tidy/").glob("*.csv"))

    for path in paths:
        print(f"\n=== {path.stem} ===")
        df = pd.read_csv(path)
        process(df)


if __name__ == "__main__":
    main()
