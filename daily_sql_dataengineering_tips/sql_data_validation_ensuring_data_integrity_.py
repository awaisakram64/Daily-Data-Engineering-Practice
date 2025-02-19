CREATE TABLE customer_orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_quantity INT CHECK (order_quantity > 0),
    CHECK (order_date <= CURRENT_DATE)
);

-- Insert valid data
tINSERT INTO customer_orders VALUES (1, 101, '2023-10-20', 10);

-- This will fail because order_quantity is 0
-- INSERT INTO customer_orders VALUES (2, 102, '2023-10-20', 0);