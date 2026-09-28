SELECT * FROM sales
LIMIT 10;

SELECT COUNT(*) AS total_rows
FROM sales;

SELECT
    store_region,
    SUM(total_revenue) AS total_revenue
FROM sales
GROUP BY store_region
ORDER BY total_revenue DESC;

SELECT
    product_category,
    SUM(total_revenue) AS total_revenue
FROM sales
GROUP BY product_category
ORDER BY total_revenue DESC;

SELECT
    product_name,
    SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY product_name
ORDER BY total_units_sold DESC
LIMIT 10;

SELECT
    date,
    SUM(total_revenue) AS daily_revenue
FROM sales
GROUP BY date
ORDER BY date;