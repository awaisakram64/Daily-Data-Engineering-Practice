ALTER TABLE sales_data
ADD COLUMN region VARCHAR(50);

-- Check the table structure after the alteration
DESCRIBE sales_data;