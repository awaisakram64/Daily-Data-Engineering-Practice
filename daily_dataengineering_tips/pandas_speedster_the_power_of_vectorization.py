import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Vectorized operation: Adding columns 'A' and 'B'
df['C'] = df['A'] + df['B']

print(df)