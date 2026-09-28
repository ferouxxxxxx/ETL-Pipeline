import pandas as pd
from pathlib import Path

RAW_FILE=Path(r"data\raw\retail-daily-sales.csv")
EXTRACTED_FILE=Path(r"data/processed/extracted_sales.csv")

def extract_data():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Dataset not found : {RAW_FILE}")


    df = pd.read_csv(RAW_FILE)

    EXTRACTED_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(EXTRACTED_FILE)

    print("Rows extracted: ", len(df))
    print("Extracted file saved to: ", EXTRACTED_FILE)


if __name__ == "__main__":
    extract_data()