-- Let's set up a simple versioned transactions table
CREATE TABLE user_transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT,
    transaction_amount DECIMAL(10, 2),
    transaction_date DATE,
    is_active BOOLEAN DEFAULT TRUE
);

-- We'll keep both active and historical records in the same table
-- Inactive records represent historical snapshots

-- Add a transaction
INSERT INTO user_transactions (user_id, transaction_amount, transaction_date) VALUES
(1, 150.00, '2023-10-01'),
(1, 200.00, '2023-10-02');

-- Version the transaction by deactivating the older record
UPDATE user_transactions SET is_active = FALSE WHERE user_id = 1 AND transaction_date = '2023-10-01';

-- Query to view active transactions
SELECT * FROM user_transactions WHERE is_active = TRUE;