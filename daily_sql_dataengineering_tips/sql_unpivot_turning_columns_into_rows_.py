WITH SampleData AS (
    SELECT 'Product1' AS Product, 10 AS [2019], 12 AS [2020], 15 AS [2021]
    UNION ALL
    SELECT 'Product2', 20, 25, 30
    UNION ALL
    SELECT 'Product3', 14, 19, 22
)
SELECT Product, Year, Sales
FROM SampleData
UNPIVOT
(Sales FOR Year IN ([2019], [2020], [2021])) AS UnpivotedData;