SELECT e.EmployeeID, e.Name, p.RecentProject 
FROM Employees e 
CROSS APPLY 
(
  SELECT TOP 1 ProjectName AS RecentProject 
  FROM Projects p 
  WHERE p.EmployeeID = e.EmployeeID 
  ORDER BY p.ProjectEndDate DESC
) p;