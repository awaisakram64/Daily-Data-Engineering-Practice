-- Create a temporal table for tracking employee salary changes
CREATE TABLE EmployeeSalaries (
  EmployeeID INT PRIMARY KEY,
  Salary INT,
  EffectiveDate DATE,
  SysStartTime DATETIME2 GENERATED ALWAYS AS ROW START,
  SysEndTime DATETIME2 GENERATED ALWAYS AS ROW END,
  PERIOD FOR SYSTEM_TIME (SysStartTime, SysEndTime)
) WITH (SYSTEM_VERSIONING = ON);

-- Query historical salary data
SELECT * FROM EmployeeSalaries FOR SYSTEM_TIME AS OF '2023-01-01';