import pandas as pd
import sqlite3

INPUT_FILE = "data/processed/cleaned_sales.csv"
DATABASE_FILE = "database/retail_sales.db"
TABLE_NAME = "sales"

def load_data():
    df = pd.read_csv(INPUT_FILE)

    connection = sqlite3.connect(DATABASE_FILE)

    df.to_sql(
        TABLE_NAME,
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print("Data loaded successfully")
    print("Rows loaded:", len(df))
    print("Database:", DATABASE_FILE)
    print("Table:", TABLE_NAME)

if __name__ == "__main__":
    load_data()