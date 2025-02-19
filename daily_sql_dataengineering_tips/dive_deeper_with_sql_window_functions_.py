WITH Sales AS (
  SELECT '2023-01-01' AS sale_date, 100 AS amount
  UNION ALL
  SELECT '2023-01-02', 150
  UNION ALL
  SELECT '2023-01-03', 200
)
SELECT 
  sale_date, 
  amount, 
  SUM(amount) OVER (ORDER BY sale_date) AS running_total
FROM Sales;