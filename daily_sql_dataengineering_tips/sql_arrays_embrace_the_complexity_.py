CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    categories TEXT[]
);

INSERT INTO products (product_name, categories) VALUES
    ('Laptop', ARRAY['Electronics', 'Computers']),
    ('Sneakers', ARRAY['Clothing', 'Shoes']),
    ('Mug', ARRAY['Household', 'Kitchen']),
    ('Smartphone', ARRAY['Electronics', 'Mobiles']);

-- Query to find products that belong to the 'Electronics' category
SELECT product_name
FROM products
WHERE 'Electronics' = ANY (categories);