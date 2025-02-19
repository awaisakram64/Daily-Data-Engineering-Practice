import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Product': ['A', 'B', 'A'],
    'Sales': [200, 150, 250],
    'Region': ['North', 'South', 'North']
}
df = pd.DataFrame(data)

# Creating a pivot table to summarize sales by product and region
df_pivot = df.pivot_table(index='Product', columns='Region', values='Sales', aggfunc='sum', fill_value=0)
print(df_pivot)