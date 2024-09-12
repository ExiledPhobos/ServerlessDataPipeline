import schedule
import time
import logging
from lambdas.lambda_1_extract import lambda_1_extract
from lambdas.lambda_2_transform import lambda_2_transform
from lambdas.lambda_3_load import lambda_3_load
from utils.visualization import plot_crypto_trend, plot_market_cap_trend

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    logging.info("Starting the data pipeline...")

    # Run each Lambda function in sequence
    try:
        # Lambda 1: Extract
        crypto_data = lambda_1_extract()
        if not crypto_data:
            logging.warning("No data extracted. Pipeline terminated.")
            return

        # Lambda 2: Transform
        transformed_data = lambda_2_transform()
        if not transformed_data:
            logging.warning("No data transformed. Pipeline terminated.")
            return

        # Lambda 3: Load
        lambda_3_load()

        # Added a clear visual separation for user input
        print("\n" + "-" * 50)
        print("Now it's time to select the cryptocurrencies for visualization.")
        print("Kindly enter the cryptocurrencies you want to plot.")
        user_input = input("Enter cryptocurrencies separated by commas (e.g., Bitcoin,Ethereum): ")
        selected_cryptos = [crypto.strip() for crypto in user_input.split(',')]

        # After loading, generate the visualizations
        logging.info(f"Generating price trend plot for {', '.join(selected_cryptos)} starting from 2024-01-01...")
        plot_crypto_trend(cryptos=selected_cryptos, start_date='2024-01-01')

        logging.info(f"Generating market cap trend plot for {', '.join(selected_cryptos)} starting from 2024-01-01...")
        plot_market_cap_trend(cryptos=selected_cryptos, start_date='2024-01-01')

        logging.info("Pipeline and visualization completed successfully!")

    except Exception as e:
        logging.error(f"Pipeline failed with error: {e}")

# Schedule the pipeline to run once a day at a specific time
schedule.every().day.at("00:00").do(run_pipeline)  # Adjust this time as needed

# The line below is for debugging purposes, replace the previous line with this one to run once every minute
# schedule.every().minute.do(run_pipeline)

logging.info("Scheduler started. Waiting for the next scheduled pipeline run...")

# Keep the script running to check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)