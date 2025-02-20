-- Assuming we have a table 'user_data' with 'user_id', 'segment' (A or B), and 'conversion' (0 or 1)
-- Our goal: compare conversion rates between segments A and B.

SELECT segment, 
       COUNT(*) AS total_users,
       SUM(conversion) AS conversions,
       AVG(conversion)::NUMERIC(5,2) AS conversion_rate
FROM user_data
GROUP BY segment;