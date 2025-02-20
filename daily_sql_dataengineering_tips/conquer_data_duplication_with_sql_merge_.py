MERGE INTO target_table AS target
USING source_table AS source
ON target.id = source.id
WHEN MATCHED THEN 
  UPDATE SET target.field1 = source.field1, target.field2 = source.field2
WHEN NOT MATCHED THEN 
  INSERT (id, field1, field2) VALUES (source.id, source.field1, source.field2);