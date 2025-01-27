# Example of using a context manager for file handling
with open('data.txt', 'r') as file:
    data = file.read()  # The file is automatically closed after this block
print(data)