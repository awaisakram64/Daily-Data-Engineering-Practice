SELECT employee_id, salary,  
CASE  
  WHEN salary > 100000 THEN 'High'  
  WHEN salary BETWEEN 60000 AND 100000 THEN 'Medium'  
  ELSE 'Low'  
END as salary_category  
FROM employees;