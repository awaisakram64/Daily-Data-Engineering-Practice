SELECT employee_id, salary, 
       SUM(salary) OVER (PARTITION BY department ORDER BY hire_date) AS running_total
FROM employees;