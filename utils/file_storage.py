import os
import json

# Create a local directory to simulate an S3 bucket for storing files
DATA_DIR = './data'

# Save data to a local directory (simulating an S3 upload)
def save_to_local_storage(data, filename):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file_path = os.path.join(DATA_DIR, filename)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Data saved to {file_path}")