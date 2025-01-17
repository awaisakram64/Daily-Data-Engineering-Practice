import dask.dataframe as dd

df = dd.read_csv('large_dataset.csv')

# Calculate mean of a column 'value' on the fly
mean_value = df['value'].mean().compute()

print("Mean of column 'value':", mean_value)