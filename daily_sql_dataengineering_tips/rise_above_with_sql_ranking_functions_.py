-- Let's find the top 3 products in each category based on sales volume!
SELECT product_name, category, sales_volume,
       RANK() OVER (PARTITION BY category ORDER BY sales_volume DESC) as rank_within_category
FROM sales_data;