-- Suppose we have two tables: 'registered_users' and 'active_users'.
-- Let's find inactive users using the EXCEPT set operation.

SELECT user_id, user_name
FROM registered_users
EXCEPT
SELECT user_id, user_name
FROM active_users;

-- This query will return all users who are registered but not active.