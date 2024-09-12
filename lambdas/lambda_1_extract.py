import requests
import logging
from utils.file_storage import save_to_local_storage

def lambda_1_extract():
    logging.info("Running Lambda 1: Extracting cryptocurrency data from API...")

    api_url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'eur',
        'ids': 'bitcoin,ethereum,binancecoin,cardano,solana,dogecoin,polkadot,litecoin,avalanche-2',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false'
    }

    try:
        # Make the request
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Extract the JSON data from the response
        crypto_data = response.json()

        # Check if the data is empty
        if not crypto_data:
            logging.warning("API response is empty.")
            return None

        logging.info("Data extraction successful.")

        # Simulate storing the data in a local S3-like folder
        save_to_local_storage(data=crypto_data, filename='crypto_raw.json')
        logging.info("Data saved to './data/crypto_raw.json'")

        return crypto_data

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
        return None