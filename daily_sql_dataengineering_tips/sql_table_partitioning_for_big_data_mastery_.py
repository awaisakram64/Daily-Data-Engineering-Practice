-- Let's partition a sales table by yearCREATE TABLE sales (
  order_id INT,
  order_date DATE,
  amount DECIMAL(10, 2)
) PARTITION BY RANGE (YEAR(order_date));

CREATE PARTITION sales_2019 VALUES LESS THAN (2020);
CREATE PARTITION sales_2020 VALUES LESS THAN (2021);
CREATE PARTITION sales_2021 VALUES LESS THAN (2022);