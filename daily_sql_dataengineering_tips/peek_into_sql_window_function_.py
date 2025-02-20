SELECT name, 
       sales, 
       RANK() OVER(PARTITION BY month ORDER BY sales DESC) as sales_rank
FROM sales_data;