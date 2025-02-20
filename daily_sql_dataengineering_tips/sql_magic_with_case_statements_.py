SELECT customer_name, purchase_amount, 
CASE 
    WHEN purchase_amount > 1000 THEN 'Premium' 
    WHEN purchase_amount BETWEEN 500 AND 1000 THEN 'Standard' 
    ELSE 'Basic' 
END AS customer_rating 
FROM purchases;