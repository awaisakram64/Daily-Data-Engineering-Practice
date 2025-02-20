CREATE TABLE inventory (
    product_id INT PRIMARY KEY,
    stock INT NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES inventory(product_id)
);

CREATE TRIGGER update_inventory_trigger
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE inventory SET stock = stock - NEW.quantity
    WHERE product_id = NEW.product_id;
END;