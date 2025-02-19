-- Suppose you have a table `products` with disorganized product codes.
-- Let's clean up these codes that should match a specific pattern (e.g., 'PROD-XXX').

SELECT 
  product_name, 
  product_code 
FROM 
  products 
WHERE 
  product_code LIKE 'PROD-%';