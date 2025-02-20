CREATE TRIGGER UpdateInventory AFTER INSERT ON Sales
FOR EACH ROW
BEGIN
   UPDATE Inventory
   SET stock = stock - NEW.quantity
   WHERE product_id = NEW.product_id;
END;