DECLARE @ExchangeRate FLOAT;
SET @ExchangeRate = 1.23; -- Assume this is the current USD to EUR rate

SELECT TotalSales, TotalSales * @ExchangeRate AS TotalSalesEUR
FROM SalesTable
WHERE SaleDate = '2023-01-01';