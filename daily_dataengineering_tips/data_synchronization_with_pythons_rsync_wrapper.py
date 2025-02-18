import subprocess

# Function to perform data synchronization using rsync
# Assuming you have rsync installed and accessible from command line

def sync_data(source, destination):
    try:
        # Constructing the rsync command
        rsync_command = [
            'rsync', '-av', '--progress', source, destination
        ]
        
        # Executing the rsync command
        subprocess.run(rsync_command, check=True)
        print("Data synchronization completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
source_path = '/path/to/source/folder/'
destination_path = '/path/to/destination/folder/'
sync_data(source_path, destination_path)