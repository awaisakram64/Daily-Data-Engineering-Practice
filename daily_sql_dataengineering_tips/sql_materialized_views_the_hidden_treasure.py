-- Create a sample Materialized View to summarize sales data
CREATE MATERIALIZED VIEW sales_summary AS
SELECT region, SUM(sales) as total_sales
FROM sales_data
GROUP BY region;