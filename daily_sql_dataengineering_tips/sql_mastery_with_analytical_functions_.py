SELECT
    order_date,
    sales_amount,
    AVG(sales_amount) OVER (ORDER BY order_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg
FROM
    sales_data;