-- Assume we have a sales table with the following columns: date, product_id, sales_amount

SELECT 
    date, 
    product_id, 
    sales_amount, 
    SUM(sales_amount) OVER (PARTITION BY product_id ORDER BY date) AS running_total
FROM 
    sales
ORDER BY 
    product_id, date;