WITH RECURSIVE employee_hierarchy AS ( 
  SELECT employee_id, manager_id, employee_name 
  FROM employees 
  WHERE manager_id IS NULL 
  UNION ALL 
  SELECT e.employee_id, e.manager_id, e.employee_name 
  FROM employees e 
  INNER JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id 
) 
SELECT * FROM employee_hierarchy;