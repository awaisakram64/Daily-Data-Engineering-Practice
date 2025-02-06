import pandas as pd

# Create two sample dataframes
df_sales = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'sales_amount': [150, 200, 300]
})

df_customers = pd.DataFrame({
    'customer_id': [2, 3, 4],
    'customer_name': ['Alice', 'Bob', 'Charlie']
})

# Merge the dataframes on customer_id
merged_df = pd.merge(df_sales, df_customers, on='customer_id', how='inner')

print(merged_df)