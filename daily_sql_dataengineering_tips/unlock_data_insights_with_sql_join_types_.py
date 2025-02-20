SELECT customers.name, orders.order_date, products.product_name 
FROM customers 
LEFT JOIN orders ON customers.id = orders.customer_id 
LEFT JOIN products ON orders.product_id = products.id;