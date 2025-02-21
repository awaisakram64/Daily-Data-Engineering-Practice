-- Imagine you have a 'sales' table with millions of rows
-- Create an index on the 'order_date' column to optimize query speed
CREATE INDEX idx_order_date ON sales(order_date);

-- Now, retrieve records quickly
SELECT * FROM sales WHERE order_date = '2022-12-01';