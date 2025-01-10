def log_line_generator(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

# Example usage:
log_generator = log_line_generator('large_log_file.txt')

# Process the first 5 lines
for _ in range(5):
    print(next(log_generator))