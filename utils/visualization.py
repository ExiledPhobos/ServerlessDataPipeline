import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Set seaborn style
sns.set(style="whitegrid")

def plot_crypto_trend(csv_file='./data/crypto_data.csv', output_file='./data/crypto_price_trend.png', cryptos=None, start_date=None, end_date=None):
    try:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(csv_file)

        # Convert 'last_updated' column to datetime and remove timezone information
        data['last_updated'] = pd.to_datetime(data['last_updated']).dt.tz_localize(None)

        # Filter by cryptocurrencies if specified
        if cryptos:
            data = data[data['name'].isin(cryptos)]
            if data.empty:
                raise ValueError("No data available for the selected cryptocurrencies.")

        # Filter by date range if specified
        if start_date:
            data = data[data['last_updated'] >= pd.to_datetime(start_date)]
        if end_date:
            data = data[data['last_updated'] <= pd.to_datetime(end_date)]

        # Check if data is empty after filtering
        if data.empty:
            raise ValueError("No data available for the selected date range.")

        # Plot price trends for the specified cryptocurrencies
        plt.figure(figsize=(12, 7))
        sns.lineplot(x='last_updated', y='current_price', hue='name', data=data)

        # Set title and labels
        title = 'Cryptocurrency Price Trends Over Time'
        if cryptos:
            title += f" for {', '.join(cryptos)}"
        plt.title(title, fontsize=18)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Price in EUR', fontsize=12)

        # Rotate the x-axis labels for better readability
        plt.xticks(rotation=45)

        # Optional grid
        plt.grid(True)

        # Save the plot to a file
        plt.tight_layout()
        plt.savefig(output_file)
        plt.show()

        logging.info(f"Price trend plot saved to {output_file}")

    except Exception as e:
        logging.error(f"Failed to generate plot: {e}")

def plot_market_cap_trend(csv_file='./data/crypto_data.csv', output_file='./data/crypto_market_cap_trend.png', cryptos=None, start_date=None, end_date=None):
    try:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(csv_file)

        # Convert 'last_updated' column to datetime and remove timezone information
        data['last_updated'] = pd.to_datetime(data['last_updated']).dt.tz_localize(None)

        # Filter by cryptocurrencies if specified
        if cryptos:
            data = data[data['name'].isin(cryptos)]
            if data.empty:
                raise ValueError("No data available for the selected cryptocurrencies.")

        # Filter by date range if specified
        if start_date:
            data = data[data['last_updated'] >= pd.to_datetime(start_date)]
        if end_date:
            data = data[data['last_updated'] <= pd.to_datetime(end_date)]

        # Check if data is empty after filtering
        if data.empty:
            raise ValueError("No data available for the selected date range.")

        # Plot market cap trends for the specified cryptocurrencies
        plt.figure(figsize=(12, 7))
        sns.lineplot(x='last_updated', y='market_cap', hue='name', data=data)

        # Set title and labels
        title = 'Cryptocurrency Market Cap Trends Over Time'
        if cryptos:
            title += f" for {', '.join(cryptos)}"
        plt.title(title, fontsize=18)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Market Cap (EUR)', fontsize=12)

        # Rotate the x-axis labels for better readability
        plt.xticks(rotation=45)

        # Optional grid
        plt.grid(True)

        # Save the plot to a file
        plt.tight_layout()
        plt.savefig(output_file)
        plt.show()

        logging.info(f"Market cap trend plot saved to {output_file}")

    except Exception as e:
        logging.error(f"Failed to generate market cap plot: {e}")