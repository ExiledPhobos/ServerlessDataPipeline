import json
import logging
from utils.file_storage import save_to_local_storage

def lambda_2_transform():
    logging.info("Running Lambda 2: Transforming cryptocurrency data...")

    input_file = './data/crypto_raw.json'

    try:
        # Load raw data
        with open(input_file, 'r') as f:
            crypto_data = json.load(f)
        logging.info("Data loaded from './data/crypto_raw.json'")

        # Transform the data
        transformed_data = []
        for coin in crypto_data:
            transformed_coin = {
                'name': coin['name'],
                'symbol': coin['symbol'],
                'current_price': coin['current_price'],
                'market_cap': coin['market_cap'],
                'price_change_percentage_24h': coin['price_change_percentage_24h'],
                'circulating_supply': coin['circulating_supply'],
                'last_updated': coin['last_updated']
            }
            transformed_data.append(transformed_coin)
        logging.info("Data transformation successful.")

        # Save the transformed data
        save_to_local_storage(data=transformed_data, filename='crypto_transformed.json')
        logging.info("Transformed data saved to './data/crypto_transformed.json'")

        return transformed_data

    except Exception as e:
        logging.error(f"Error processing data: {e}")
        return None