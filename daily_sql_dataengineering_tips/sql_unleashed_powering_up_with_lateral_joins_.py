SELECT c.category_id, c.category_name, t.top_product
FROM categories c
CROSS JOIN LATERAL (
  SELECT p.product_name AS top_product
  FROM products p
  WHERE p.category_id = c.category_id
  ORDER BY p.sales DESC
  LIMIT 1
) t;