SELECT sale_id, amount, 
  CASE 
    WHEN amount >= 10000 THEN 'High' 
    WHEN amount >= 5000 THEN 'Medium' 
    ELSE 'Low' 
  END AS sale_category 
FROM sales;