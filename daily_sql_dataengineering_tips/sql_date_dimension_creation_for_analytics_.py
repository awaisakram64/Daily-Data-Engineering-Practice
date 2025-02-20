CREATE TABLE DateDimension (
    DateID INT NOT NULL PRIMARY KEY,
    Date DATE NOT NULL,
    DayOfWeek VARCHAR(10),
    MonthName VARCHAR(15),
    Quarter INT
);

INSERT INTO DateDimension (DateID, Date, DayOfWeek, MonthName, Quarter)
WITH RECURSIVE DateSeries AS (
    SELECT CAST('2023-01-01' AS DATE) AS Date
    UNION ALL
    SELECT Date + INTERVAL 1 DAY
    FROM DateSeries
    WHERE Date < '2023-12-31'
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY Date) AS DateID,
    Date,
    DATE_FORMAT(Date, '%W') AS DayOfWeek,
    DATE_FORMAT(Date, '%M') AS MonthName,
    QUARTER(Date) AS Quarter
FROM DateSeries;

SELECT * FROM DateDimension LIMIT 5;