import pandas as pd

# Sample data: Sales records
sales_data = {
    'Region': ['East', 'West', 'East', 'West', 'East'],
    'Sales': [2342, 4351, 1234, 4324, 5435]
}

# Create a DataFrame
sales_df = pd.DataFrame(sales_data)

# Group by 'Region' and sum the 'Sales'
sales_summary = sales_df.groupby('Region').sum()

# Print the results
print(sales_summary)