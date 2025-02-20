-- Consider a table `users` with columns: id, name, email, and phone
-- Some email and phone entries might be NULL. Use COALESCE to ensure we have a contact method.

SELECT 
    id, 
    name,
    COALESCE(email, phone, 'No Contact Info') AS contact_method
FROM 
    users;

-- Now use CASE to achieve the same result.

SELECT 
    id, 
    name,
    CASE 
        WHEN email IS NOT NULL THEN email
        WHEN phone IS NOT NULL THEN phone
        ELSE 'No Contact Info'
    END AS contact_method
FROM 
    users;