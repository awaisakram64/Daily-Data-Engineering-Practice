CREATE TRIGGER update_inventory AFTER INSERT ON sales 
FOR EACH ROW BEGIN
  UPDATE products 
  SET stock = stock - NEW.quantity 
  WHERE product_id = NEW.product_id;
END;