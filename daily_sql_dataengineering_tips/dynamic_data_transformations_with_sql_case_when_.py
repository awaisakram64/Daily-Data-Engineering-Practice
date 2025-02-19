SELECT product_id, product_code, 
       CASE 
           WHEN product_code = 'A' THEN 'Category A'
           WHEN product_code = 'B' THEN 'Category B'
           ELSE 'Other Category'
       END AS product_category
FROM products;