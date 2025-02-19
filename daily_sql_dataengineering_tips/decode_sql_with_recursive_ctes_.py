WITH RECURSIVE EmployeeHierarchy AS (  
  SELECT employee_id, name, manager_id  
  FROM employees  
  WHERE manager_id IS NULL  
  UNION ALL  
  SELECT e.employee_id, e.name, e.manager_id  
  FROM employees e  
  INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.employee_id)  
SELECT * FROM EmployeeHierarchy;