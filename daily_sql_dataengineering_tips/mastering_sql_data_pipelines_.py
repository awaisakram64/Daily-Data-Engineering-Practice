-- Imagine we have a table called 'raw_data' and you need to clean and aggregate this data for reporting.

CREATE TABLE IF NOT EXISTS cleaned_data AS
SELECT 
    id,
    name,
    SUM(sales) as total_sales,
    AVG(rating) as average_rating
FROM raw_data
WHERE date > '2023-01-01'
GROUP BY id, name;

-- This query creates a new table 'cleaned_data' with aggregated data ready for analysis.