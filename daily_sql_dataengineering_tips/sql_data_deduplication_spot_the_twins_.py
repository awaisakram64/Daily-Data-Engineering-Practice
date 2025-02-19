SELECT column1, column2, column3, COUNT(*)
FROM data_table
GROUP BY column1, column2, column3
HAVING COUNT(*) > 1;