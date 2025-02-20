-- Sample tables: Products and Suppliers

CREATE TABLE Products (
  ProductID INT,
  ProductName VARCHAR(255)
);

CREATE TABLE Suppliers (
  SupplierID INT,
  SupplierName VARCHAR(255)
);

-- Populating tables
INSERT INTO Products (ProductID, ProductName) VALUES
(1, 'Apples'),
(2, 'Bananas');

INSERT INTO Suppliers (SupplierID, SupplierName) VALUES
(1, 'Fresh Farms'),
(2, 'Organic Foods');

-- CROSS JOIN example
SELECT ProductName, SupplierName
FROM Products
CROSS JOIN Suppliers;