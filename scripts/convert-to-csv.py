import pandas as pd

RAW_DIR = "data/raw"

FILES = {
    "csub": "FOIA #22-01101_TLR_Controlled Substances (5).xlsx",
    "chem": "FOIA #22-01101_TLR_Chemicals (9).xlsx",
}

SHEET_NAMES = {
    "thefts-by-business-and-loss-type": "Theft by Bus Act-Loss Type",
    "thefts-by-state-and-business": "No of Thefts by State-Bus Act",
    "thefts-by-state-and-loss-type": "No of Thefts by State-Loss Type",
    "quantity-lost": "Total Quantity Lost by State",
}


def load_raw(file_name: str, sheet_name: str) -> pd.DataFrame:
    return pd.read_excel(f"{RAW_DIR}/{file_name}", sheet_name=sheet_name, skiprows=1)


def convert_to_tidy(df: pd.DataFrame) -> pd.DataFrame:
    # Next two lines figure out the number of columns
    # that come before the first year-column
    year_cols = [c for c in df.columns if str(c)[0] == "2"]
    index_count = list(df.columns).index(year_cols[0])

    main_cols = {
        c: c.strip().lower().replace(" ", "_") for c in df.columns[:index_count]
    }
    final_col = list(main_cols.values())[index_count - 1]

    return (
        df.rename(
            columns={
                "NUMBER OF THEFTS": "TOTAL 2010–SEP 2022",
                "TOTAL QUANTITY LOST": "TOTAL 2010–SEP 2022",
                **main_cols,
            }
        )
        .drop(columns=["TOTAL 2010–SEP 2022"])
        .dropna(subset=[final_col])
        .ffill()
        .melt(id_vars=main_cols.values(), var_name="period", value_name="count")
    )


def restructure_quantities(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.assign(
            unit_of_measure=lambda df: df["unit_of_measure"].str.lower(),
        )
        .set_index(
            ["state", "business_activity", "loss_type", "period", "unit_of_measure"]
        )["count"]
        .unstack()
        .reset_index()
        .fillna(0)
    )


def main() -> None:
    for file_key, file_name in FILES.items():
        for sheet_key, sheet_name in SHEET_NAMES.items():
            raw = load_raw(file_name, sheet_name)
            tidy = convert_to_tidy(raw)

            # To fix inconsistency in casing between the two files
            if "loss_type" in tidy.columns:
                tidy["loss_type"] = tidy["loss_type"].str.upper()

            if sheet_key == "quantity-lost":
                tidy = restructure_quantities(tidy)

            tidy.to_csv(f"data/tidy/{file_key}-{sheet_key}.csv", index=False)


if __name__ == "__main__":
    main()
