CREATE SEQUENCE customer_id_seq START WITH 1 INCREMENT BY 1;

SELECT nextval('customer_id_seq') AS new_customer_id;