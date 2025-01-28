def search_logs(file_path, keyword):
    with open(file_path, 'r') as file:  # Open the log file for reading
        for line in file:  # Read the file line by line
            if keyword in line:  # Check if the keyword is in the current line
                print(line.strip())  # Print the line without leading/trailing spaces

# Sample usage
# Assuming 'system_logs.txt' is a file containing log entries
search_logs('system_logs.txt', 'ERROR')