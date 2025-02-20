-- Let's get started with a simple example to sum sales by region!
SELECT region, SUM(sales) as total_sales
FROM sales_data
GROUP BY region;