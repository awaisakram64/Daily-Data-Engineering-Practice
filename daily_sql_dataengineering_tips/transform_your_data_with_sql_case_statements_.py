SELECT order_id, total_sales,
CASE
  WHEN total_sales > 1000 THEN 'High'
  WHEN total_sales BETWEEN 500 AND 1000 THEN 'Medium'
  ELSE 'Low'
END AS sales_category
FROM sales_table;