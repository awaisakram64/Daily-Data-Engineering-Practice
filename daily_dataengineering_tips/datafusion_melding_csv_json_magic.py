import pandas as pd
import json

# Sample CSV data
csv_data = """id,name,sales
1,John,500
2,Jane,600
"""

# Sample JSON data
json_data = '[{"id": 1, "feedback": "Great service!"}, {"id": 2, "feedback": "Very happy with the product."}]'

# Create DataFrame from CSV
csv_df = pd.read_csv(pd.compat.StringIO(csv_data))

# Create DataFrame from JSON
json_df = pd.DataFrame(json.loads(json_data))

# Merging the data on 'id'
merged_data = pd.merge(csv_df, json_df, on='id')

print(merged_data)