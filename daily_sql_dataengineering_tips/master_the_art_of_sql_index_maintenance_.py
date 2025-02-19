-- Assume we have a SQL Server database with a table named 'Orders'.
-- This SQL snippet helps you rebuild fragmented indexes on that table.

ALTER INDEX ALL ON Orders
REBUILD;