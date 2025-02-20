-- Sample SQL Merge Statement to Synchronize Two Tables
MERGE INTO target_table AS target
USING source_table AS source
ON target.id = source.id
WHEN MATCHED THEN
    UPDATE SET target.name = source.name, target.value = source.value
WHEN NOT MATCHED THEN
    INSERT (id, name, value) VALUES (source.id, source.name, source.value);