CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10, 2)
);

-- Create an index on order_date to speed up queries
CREATE INDEX idx_order_date ON orders(order_date);

-- Let's run a query to see how the index improves performance
EXPLAIN SELECT * FROM orders WHERE order_date = '2023-01-15';