import csv
import logging
import json
import os

def lambda_3_load():
    logging.info("Running Lambda 3: Loading data into CSV...")

    input_file = './data/crypto_transformed.json'
    output_file = './data/crypto_data.csv'

    try:
        # Load transformed data
        with open(input_file, 'r') as f:
            transformed_data = json.load(f)
        logging.info("Data loaded from './data/crypto_transformed.json'")

        # Check if the CSV file already exists
        file_exists = os.path.isfile(output_file)

        # Open CSV in append mode
        with open(output_file, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=transformed_data[0].keys())

            # Write header only if the file does not exist or is empty
            if not file_exists:
                writer.writeheader()

            # Write the new rows of data
            writer.writerows(transformed_data)
        logging.info(f"Data successfully appended to {output_file}")

    except Exception as e:
        logging.error(f"Error loading data: {e}")