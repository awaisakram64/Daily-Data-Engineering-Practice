def clean_data(data):
    return [item.strip().capitalize() for item in data]

def filter_data(data):
    return [item for item in data if len(item) > 3]

def export_data(data):
    return ', '.join(data)

data = ['apple  ', '  banana', 'ki', 'strawberry', '  ', 'peach ']

# Chaining functions for a streamlined data pipeline
cleaned = clean_data(data)
filtered = filter_data(cleaned)
result = export_data(filtered)
print(result)