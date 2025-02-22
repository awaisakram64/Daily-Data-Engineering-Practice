SELECT customer_id, sale_amount FROM north_region_sales
UNION
SELECT customer_id, sale_amount FROM south_region_sales;