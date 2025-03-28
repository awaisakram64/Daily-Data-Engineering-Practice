SELECT product_id, product_name, 
       (SELECT COUNT(order_id) 
        FROM orders 
        WHERE orders.product_id = products.product_id) AS order_count 
FROM products 
WHERE (SELECT COUNT(order_id) 
       FROM orders 
       WHERE orders.product_id = products.product_id) > 10;