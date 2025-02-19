-- Example of a SQL dynamic query using SQL Server's sp_executesql
declare @sql nvarchar(1000);
declare @tableName nvarchar(100) = 'Employees';

set @sql = N'SELECT * FROM ' + @tableName;

exec sp_executesql @sql;