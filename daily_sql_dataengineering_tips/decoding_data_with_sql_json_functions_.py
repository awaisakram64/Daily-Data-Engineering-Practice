-- Assume you have a table named 'orders' with a JSON column named 'order_details'. Let's extract specific information from that JSON using SQL!

SELECT
  order_id,
  JSON_VALUE(order_details, '$.customer_name') AS customer_name,
  JSON_VALUE(order_details, '$.total_amount') AS total_amount
FROM
  orders;