SELECT *
FROM (
    SELECT Category, Year, Amount
    FROM Sales
) AS SourceTable
PIVOT (
    SUM(Amount)
    FOR Year IN ([2021], [2022], [2023])
) AS PivotTable;