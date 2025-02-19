CREATE TABLE log_data (
  id SERIAL PRIMARY KEY,
  log_details JSONB
);

INSERT INTO log_data(log_details) VALUES
  ('{"event": "login", "user": "alice", "status": "success"}'),
  ('{"event": "logout", "user": "bob", "status": "success"}'),
  ('{"event": "login", "user": "carol", "status": "failure"}');

-- Query to extract event types from JSON data
SELECT log_details->>'event' AS event_type
FROM log_data;