import pandas as pd

raw = pd.read_csv("data/processed/extracted_sales.csv")
cleaned = pd.read_csv("data/processed/cleaned_sales.csv")

print("Original rows:", len(raw))
print("Cleaned rows:", len(cleaned))
print("Rows removed:", len(raw) - len(cleaned))

print("\nMissing values in original data:")
print(raw.isnull().sum())

print("\nDuplicate rows in original data:")
print(raw.duplicated().sum())

print("\nInvalid values:")

print("Negative units sold:", (raw["units_sold"] < 0).sum())
print("Negative unit price:", (raw["unit_price"] < 0).sum())
print(
    "Invalid discount:",
    ((raw["discount_pct"] < 0) | (raw["discount_pct"] > 100)).sum()
)