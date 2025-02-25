-- Create an index on the 'last_name' column of the 'customers' table
CREATE INDEX idx_last_name ON customers (last_name);

-- Execute a query that benefits from the index
SELECT * FROM customers WHERE last_name = 'Doe';