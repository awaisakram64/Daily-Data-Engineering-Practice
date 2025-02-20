-- Retrieve the first 10 rows from the orders table
SELECT * FROM orders
OFFSET 0 ROWS
FETCH NEXT 10 ROWS ONLY;