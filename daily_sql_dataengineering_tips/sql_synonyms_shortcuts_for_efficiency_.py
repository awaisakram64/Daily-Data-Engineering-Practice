-- Creating a synonym for a long table name
CREATE SYNONYM cust_txn FOR customer_transactions_master_2023;

-- Now using the synonym in a query
db2 => SELECT * FROM cust_txn WHERE transaction_id = 123456;