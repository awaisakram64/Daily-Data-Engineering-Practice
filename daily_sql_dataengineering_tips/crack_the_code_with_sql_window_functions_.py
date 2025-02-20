SELECT employee_id, salary, SUM(salary) OVER (PARTITION BY department ORDER BY salary) AS running_total
FROM employees;