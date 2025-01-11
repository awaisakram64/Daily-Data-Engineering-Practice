import pandas as pd

data = {
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Chicago', 'Chicago'],
    'Sales': [100, 200, 150, 300, 250, 350]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'City' and sum up the 'Sales'
result = df.groupby('City').agg({'Sales': 'sum'})

print(result)