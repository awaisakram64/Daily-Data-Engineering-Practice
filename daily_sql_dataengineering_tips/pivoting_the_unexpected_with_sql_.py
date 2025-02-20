WITH SalesData AS (
  SELECT 'Apple' AS Product, '2023-01' AS Period, 120 AS Quantity
  UNION ALL
  SELECT 'Banana', '2023-01', 150
  UNION ALL
  SELECT 'Apple', '2023-02', 200
  UNION ALL
  SELECT 'Banana', '2023-02', 180
)
SELECT *
FROM SalesData
PIVOT (
  SUM(Quantity)
  FOR Period IN ('2023-01', '2023-02')
) AS PivotTable;