-- Suppose you have a large table `orders` with millions of rows:

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

-- Without an index, searching for all orders by a specific customer could be slow:
SELECT * FROM orders WHERE customer_id = 102;

-- Let's create an index on the `customer_id` column to speed this up:
CREATE INDEX idx_customer_id ON orders(customer_id);

-- Now, try running the same query again and observe the performance boost!