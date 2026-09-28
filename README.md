# E-Commerce Sales Analytics Pipeline

An automated batch ETL and analytics pipeline for retail sales data using Python, SQLite, SQL, FastAPI, and Windows Task Scheduler.

## Project Overview

This project demonstrates a complete data analytics workflow:

```text
Raw CSV
   ↓
Extract
   ↓
Transform & Data Cleaning
   ↓
SQLite Database
   ↓
SQL Analysis
   ↓
FastAPI
   ↓
Automated Scheduled ETL
```

The pipeline takes raw retail sales data, validates and cleans it, loads it into a SQLite database, performs analytical queries, and exposes the data through a REST API.

## Technologies Used

* Python
* Pandas
* SQLite
* SQL
* FastAPI
* Uvicorn
* Windows Task Scheduler
* Git & GitHub

## Dataset

The dataset contains 1,000 retail sales records with the following fields:

* `date`
* `store_id`
* `store_region`
* `product_category`
* `product_name`
* `units_sold`
* `unit_price`
* `total_revenue`
* `discount_pct`

During transformation, invalid and incomplete records are removed and additional revenue validation fields are calculated.

## ETL Pipeline

### 1. Extract

`src/extract.py`

Reads the raw CSV dataset and creates:

```text
data/processed/extracted_sales.csv
```

### 2. Transform

`src/transform.py`

The transformation stage:

* Removes unnecessary columns
* Converts dates to the correct format
* Converts numeric columns to numeric data types
* Removes duplicate records
* Handles missing required values
* Removes invalid numerical values
* Validates discount percentages
* Calculates expected revenue
* Calculates the difference between reported and calculated revenue

The original dataset contains 1,000 records. After cleaning, 999 valid records remain.

### 3. Load

`src/load.py`

Loads the cleaned dataset into SQLite.

Database:

```text
database/retail_sales.db
```

Table:

```text
sales
```

### 4. Pipeline

`src/pipeline.py`

Runs the complete ETL workflow:

```text
Extract → Transform → Load
```

## SQL Analysis

SQL queries are stored in:

```text
sql/analysis.sql
```

Current analysis includes:

* Total number of records
* Revenue by region
* Revenue by product category
* Top products by units sold
* Daily revenue

## FastAPI

The project exposes the database through a REST API.

API application:

```text
src/api.py
```

Start the API from the project root:

```powershell
python -m uvicorn src.api:app --reload
```

The API runs at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### Available Endpoints

#### Home

```text
GET /
```

Returns the API status.

#### Sales

```text
GET /sales
```

Returns sales records.

Example:

```text
/sales?limit=10
```

Filter by region:

```text
/sales?region=North
```

Filter by date:

```text
/sales?start_date=2025-01-01&end_date=2025-01-31
```

#### Total Revenue

```text
GET /revenue
```

Returns total revenue across the dataset.

#### Revenue by Region

```text
GET /revenue/region
```

Returns revenue grouped by store region.

#### Revenue by Category

```text
GET /revenue/category
```

Returns revenue grouped by product category.

## Automation

The ETL pipeline is automated using Windows Task Scheduler.

Batch file:

```text
run_pipeline.bat
```

The scheduled task executes the complete pipeline automatically.

This allows the workflow to be run without manually executing the Python scripts.

## Project Structure

```text
e_commerce/
│
├── data/
│   ├── raw/
│   │   └── retail-daily-sales.csv
│   │
│   └── processed/
│       ├── extracted_sales.csv
│       └── cleaned_sales.csv
│
├── database/
│   └── retail_sales.db
│
├── sql/
│   └── analysis.sql
│
├── src/
│   ├── api.py
│   ├── check_cleaning.py
│   ├── extract.py
│   ├── inspect_data.py
│   ├── load.py
│   ├── pipeline.py
│   └── transform.py
│
├── .gitignore
├── requirements.txt
├── run_pipeline.bat
└── README.md
```

## Installation

Clone the repository:

```powershell
git clone https://github.com/ferouxxxxxx/ETL-Pipeline.git
```

Move into the project:

```powershell
cd ETL-Pipeline
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Running the ETL Pipeline

From the project root:

```powershell
python src/pipeline.py
```

Or run the batch file:

```powershell
.\run_pipeline.bat
```

## Data Quality Checks

Run:

```powershell
python src/check_cleaning.py
```

This checks:

* Missing values
* Duplicate records
* Negative units sold
* Negative prices
* Invalid discount percentages
* Number of records removed during cleaning

## Requirements

Dependencies are listed in:

```text
requirements.txt
```

Main dependencies:

* pandas
* fastapi
* uvicorn

SQLite is included with Python and does not require a separate installation.

## Future Improvements

Planned improvements include:

* Data visualization dashboard
* More advanced SQL analytics
* API authentication
* Logging and monitoring
* Automated data quality tests
* PostgreSQL support
* Airflow-based orchestration
* Docker deployment
* Cloud deployment
* Business KPI dashboard

## Author

Fahad Manzoor
