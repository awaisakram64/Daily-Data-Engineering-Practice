CREATE TABLE daily_transactions (
    transaction_id INT,
    transaction_date DATE,
    amount DECIMAL(10, 2)
) PARTITION BY RANGE (YEAR(transaction_date)) (
    PARTITION p2019 VALUES LESS THAN (2020),
    PARTITION p2020 VALUES LESS THAN (2021),
    PARTITION p2021 VALUES LESS THAN (2022)
);

-- Example query to find transactions in 2020
SELECT * FROM daily_transactions 
WHERE transaction_date BETWEEN '2020-01-01' AND '2020-12-31';