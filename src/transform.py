import pandas as pd
from pathlib import Path

EXTRACTED_FILE = Path("data/processed/extracted_sales.csv")
TRANSFORMED_FILE = Path("data/processed/cleaned_sales.csv")

def transform_data():
    if not EXTRACTED_FILE.exists():
        raise FileNotFoundError(f"File not found: {EXTRACTED_FILE}")

    df = pd.read_csv(EXTRACTED_FILE)

    df = df.drop(columns=["Unnamed: 0"], errors="ignore")

    df["date"] = pd.to_datetime(df["date"])

    numeric_columns= [
        "units_sold",
        "unit_price",
        "total_revenue",
        "discount_pct"
    ]

    for column in numeric_columns:
        df[column]= pd.to_numeric(df[column])

    df = df.drop_duplicates()

    df = df.dropna(subset=[
        "date",
        "store_id",
        "product_category",
        "product_name",
        "units_sold",
        "unit_price"
    ])

    df = df[df["units_sold"] >= 0]
    df = df[df["unit_price"] >= 0]
    df = df[df["discount_pct"].between(0, 100)]

    df["calculated_revenue"] = (
        df["units_sold"]
        * df["unit_price"]
        * (1 - df["discount_pct"] / 100)
    )

    df["revenue_difference"] = (
        df["total_revenue"] - df["calculated_revenue"]
    )

    df["calculated_revenue"] = df["calculated_revenue"].round(2)
    df["revenue_difference"] = df["revenue_difference"].round(2)

    df.to_csv("data/processed/cleaned_sales.csv", index=False)

    print("Transformation complete")
    print("Rows:", len(df))
    print("Saved to: data/processed/cleaned_sales.csv")


if __name__=="__main__":
    transform_data()