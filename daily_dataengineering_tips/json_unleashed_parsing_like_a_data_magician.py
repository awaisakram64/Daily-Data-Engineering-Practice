import json

# Sample JSON data (as it might come from an API or data file)
json_data = '{"name": "Alice", "age": 30, "city": "Wonderland"}'

# Parse JSON into a Python dictionary
parsed_data = json.loads(json_data)

# Access data
name = parsed_data['name']
age = parsed_data['age']
city = parsed_data['city']

print(f"Name: {name}, Age: {age}, City: {city}")