SELECT 
  COALESCE(user_name, 'Unknown User') AS resolved_name, 
  COALESCE(email, 'No Email Provided') AS resolved_email 
FROM users;