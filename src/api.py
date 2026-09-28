from fastapi import FastAPI
import sqlite3

app = FastAPI(title="RETAIL SALES ANALYTICS API")

DATABASE= "database/retail_sales.db"

def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

@app.get("/")
def home():
    return {
        "message": "RETAIL SALES ANALYTICS API",
        "status": "running"
    }

@app.get("/sales")
def get_sales(
    limit: int = 10,
    region: str = None,
    start_date: str = None,
    end_date: str = None
):
    connection = get_connection()

    query = "SELECT * FROM sales WHERE 1=1"
    parameters = []

    if region:
        query += " AND store_region = ?"
        parameters.append(region)

    if start_date:
        query += " AND date >= ?"
        parameters.append(start_date)

    if end_date:
        query += " AND date <= ?"
        parameters.append(end_date)

    query += " LIMIT ?"
    parameters.append(limit)

    cursor = connection.execute(query, parameters)

    rows = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return rows

@app.get("/revenue/region")
def get_revenue_by_region():
    connection= get_connection()

    cursor = connection.execute("""
        SELECT
            store_region,
            SUM(total_revenue) AS total_revenue
        FROM sales
        GROUP BY store_region
        ORDER BY total_revenue DESC
        """)

    rows = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return rows

@app.get("/revenue/category")
def get_revenue_by_category():
    connection = get_connection()

    cursor = connection.execute("""
        SELECT
            product_category,
            SUM(total_revenue) AS total_revenue
        FROM sales
        GROUP BY product_category
        ORDER BY total_revenue DESC
    """)

    rows = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return rows