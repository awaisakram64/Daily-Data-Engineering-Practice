-- Imagine a table 'EMPLOYEES' with columns 'NAME', 'DEPARTMENT', and 'SALARY'.
-- We're going to filter employees based on dynamic conditions.

SELECT NAME, DEPARTMENT, SALARY
FROM EMPLOYEES
WHERE (DEPARTMENT = 'Engineering' OR ? IS NULL)
   AND (SALARY > ? OR ? IS NULL);