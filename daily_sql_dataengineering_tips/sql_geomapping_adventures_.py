-- Assume we have a table named 'locations' with columns 'id', 'name', and 'coordinates' (a geometry type).
SELECT name
FROM locations
WHERE ST_Distance(coordinates, ST_GeomFromText('POINT(1 1)')) < 1000;