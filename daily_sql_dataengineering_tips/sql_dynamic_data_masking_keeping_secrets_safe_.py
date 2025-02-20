CREATE TABLE CustomerData (
    CustomerID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Email NVARCHAR(100) MASKED WITH (FUNCTION = 'email()'),
    CreditCardNumber VARCHAR(16) MASKED WITH (FUNCTION = 'default()')
);

-- Querying the table with a user that has mask permission
SELECT CustomerID, Name, Email, CreditCardNumber FROM CustomerData;