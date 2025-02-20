-- Create a sample table for server performance dataCREATE TABLE server_performance (timestamp TIMESTAMP, cpu_usage INT);

-- Insert sample dataINSERT INTO server_performance (timestamp, cpu_usage) VALUES ('2023-01-01 00:00:00', 20), ('2023-01-01 01:00:00', 35), ('2023-01-01 02:00:00', 40);

-- Query to find average CPU usage by hourSELECT DATE_TRUNC('hour', timestamp) AS hour, AVG(cpu_usage) AS avg_cpu_usage FROM server_performance GROUP BY hour ORDER BY hour;