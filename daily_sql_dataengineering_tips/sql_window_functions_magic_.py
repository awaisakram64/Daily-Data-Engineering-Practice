SELECT employee_id, department, salary, SUM(salary) OVER (PARTITION BY department) AS department_total 
FROM employees;