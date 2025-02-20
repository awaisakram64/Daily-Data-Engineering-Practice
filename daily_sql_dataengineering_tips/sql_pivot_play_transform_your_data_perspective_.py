SELECT Product, [January], [February], [March]
FROM (
    SELECT Product, Month, Sales
    FROM SalesData
) AS SourceTable
PIVOT (
    SUM(Sales)
    FOR Month IN ([January], [February], [March])
) AS PivotTable;