SELECT EmployeeID, FirstName, LastName, Salary,
       SUM(Salary) OVER (PARTITION BY Department ORDER BY Salary DESC) AS DepartmentSalaryRunningTotal
FROM Employees;