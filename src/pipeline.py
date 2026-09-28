from extract import extract_data
from transform import transform_data
from load import load_data

print("Starting ETL pipeline...")

print("\n--- EXTRACT ---")
extract_data()

print("\n--- TRANSFORM ---")
transform_data()

print("\n--- LOAD ---")
load_data()

print("\nETL pipeline completed successfully.")