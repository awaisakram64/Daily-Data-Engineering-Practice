-- Start by creating a Star Schema for a retail database
-- Create a fact table for sales
CREATE TABLE SalesFact (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    DateID INT,
    StoreID INT,
    Amount DECIMAL(10, 2)
);

-- Create a dimension table for products
CREATE TABLE ProductDim (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Category VARCHAR(100)
);

-- Create a dimension table for dates
CREATE TABLE DateDim (
    DateID INT PRIMARY KEY,
    Date DATE,
    Year INT,
    Month VARCHAR(10),
    Day INT
);

-- Create a dimension table for stores
CREATE TABLE StoreDim (
    StoreID INT PRIMARY KEY,
    StoreName VARCHAR(255),
    Location VARCHAR(255)
);

-- Query to find total sales amount by product category
SELECT pd.Category, SUM(sf.Amount) AS TotalSales
FROM SalesFact sf
JOIN ProductDim pd ON sf.ProductID = pd.ProductID
GROUP BY pd.Category;