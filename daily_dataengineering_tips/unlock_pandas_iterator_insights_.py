import pandas as pd

# Read a large CSV file in chunks
data_chunks = pd.read_csv('large_dataset.csv', chunksize=10000)

# Process each chunk
for chunk in data_chunks:
    # Example operation: calculate and print the mean of a column named 'value'
    print(chunk['value'].mean())