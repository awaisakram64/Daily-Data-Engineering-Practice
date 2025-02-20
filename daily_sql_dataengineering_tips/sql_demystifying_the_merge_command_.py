-- Assume we have two tables: staging_sales and main_sales
-- Both tables have the columns: sale_id, product_id, quantity, sale_date

MERGE INTO main_sales m
USING staging_sales s
ON m.sale_id = s.sale_id
WHEN MATCHED THEN
    UPDATE SET m.quantity = s.quantity, m.sale_date = s.sale_date
WHEN NOT MATCHED THEN
    INSERT (sale_id, product_id, quantity, sale_date)
    VALUES (s.sale_id, s.product_id, s.quantity, s.sale_date)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;