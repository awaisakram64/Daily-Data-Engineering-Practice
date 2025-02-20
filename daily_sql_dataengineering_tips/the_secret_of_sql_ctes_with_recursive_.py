WITH RECURSIVE factorial_cte AS (
  SELECT 1 AS n, 1 AS factorial
  UNION ALL
  SELECT n + 1, (n + 1) * factorial
  FROM factorial_cte
  WHERE n < 5
)
SELECT * FROM factorial_cte;