import json

# Sample JSON data
json_data = '{"name": "Alice", "occupation": "Data Engineer", "skills": ["Python", "SQL", "ETL"]}'

# Parse JSON into a Python dictionary
parsed_data = json.loads(json_data)

# Access and print specific data
name = parsed_data['name']
skills = ', '.join(parsed_data['skills'])

print(f"Name: {name}")
print(f"Skills: {skills}")