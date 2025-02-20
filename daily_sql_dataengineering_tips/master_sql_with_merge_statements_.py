-- Assume we have two tables: source_data and target_data
MERGE INTO target_data AS target
USING source_data AS source
ON target.id = source.id
WHEN MATCHED THEN
    UPDATE SET target.value = source.value
WHEN NOT MATCHED BY TARGET THEN
    INSERT (id, value) VALUES (source.id, source.value)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;