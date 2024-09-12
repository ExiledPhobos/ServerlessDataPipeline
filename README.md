---

# Serverless Data Pipeline for Cryptocurrency Data

### Overview

This project simulates a serverless data processing pipeline to automate the extraction, transformation, and storage of cryptocurrency data from a public API. The pipeline collects real-time data for popular cryptocurrencies and stores it in a CSV file to create a historical record. It also generates data visualizations to track cryptocurrency price and market capitalization trends over time.

The pipeline runs automatically on a daily schedule and is built using Python, relying on several well-known libraries for data handling and visualization.

### Key Features

- **Data Extraction**: Fetches real-time cryptocurrency data (prices, market caps, etc.) from the CoinGecko API.
- **Data Transformation**: Formats and processes the extracted data to make it suitable for analysis and storage.
- **Data Loading**: Appends the processed data to a CSV file (`crypto_data.csv`), keeping a historical log of cryptocurrency prices and market caps.
- **Data Visualization**: Automatically generates trend charts for cryptocurrency prices and market caps using `matplotlib` and `seaborn`.
- **Automation**: The pipeline is scheduled to run daily at midnight using the `schedule` library, ensuring up-to-date data collection without manual intervention.

### Project Structure

```bash
ServerlessDataPipeline/
├── data/                           # Folder to store raw, transformed data and visualizations
├── lambdas/
│   ├── lambda_1_extract.py          # Fetches cryptocurrency data from the API
│   ├── lambda_2_transform.py        # Processes raw API data into structured format
│   ├── lambda_3_load.py             # Appends the structured data to a CSV file
├── utils/
│   ├── file_storage.py              # Helper functions for saving/loading data
│   ├── visualization.py             # Functions to generate data visualizations
├── tests/
│   ├── test_lambda_1_extract.py     # Unit test for lambda 1 (data extraction)
│   ├── test_lambda_2_transform.py   # Unit test for lambda 2 (data transformation)
│   ├── test_lambda_3_load.py        # Unit test for lambda 3 (data loading)
├── main.py                          # Entry point for running the pipeline
├── requirements.txt                 # Python dependencies
└── README.md                        # Project overview and setup instructions
```

### How the Pipeline Works

1. **Data Extraction (Lambda 1)**: The pipeline fetches the latest cryptocurrency data from the CoinGecko API. It retrieves prices, market capitalization, and other metrics for a selection of popular cryptocurrencies like Bitcoin and Ethereum.
   
2. **Data Transformation (Lambda 2)**: The raw data from the API is transformed into a structured format that can be easily analyzed. For example, the data is cleaned, and only relevant fields (like price, market cap, and supply) are kept.

3. **Data Loading (Lambda 3)**: The structured data is appended to a CSV file (`crypto_data.csv`) that maintains a historical record of cryptocurrency prices and market caps. Each run of the pipeline adds new data to this file without overwriting the previous records.

4. **Data Visualization**: The pipeline generates visualizations of cryptocurrency price trends and market cap trends using `matplotlib` and `seaborn`. These visualizations are saved as PNG files in the `data/` folder, giving users an easy way to track how the value of cryptocurrencies changes over time.

5. **Automation**: The entire pipeline is automated to run every day at midnight using the `schedule` library. This ensures that the data and visualizations are always up to date without requiring manual execution.

### Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.x
- `pip` (Python package manager)

### Setup Instructions

1. **Clone the Repository**:
```bash
git clone https://github.com/ExiledPhobos/ServerlessDataPipeline.git
cd ServerlessDataPipeline
```

2. **Set Up Virtual Environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate
```

3. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the Pipeline Manually**:
You can run the pipeline manually to test it:
```bash
python main.py
```

### Running the Automated Pipeline

By default, the pipeline is set to run every day at midnight. You can change the schedule in `main.py` using the `schedule` library:
```python
schedule.every().day.at("00:00").do(run_pipeline)
```

This ensures that the latest cryptocurrency data is fetched, processed, and stored daily, with updated visualizations generated automatically.

### Example Output

- **CSV Data**: The `crypto_data.csv` file in the `data/` folder contains a growing historical record of cryptocurrency prices and market caps. Each new pipeline run appends data to this file.
  
- **Visualizations**: Two visualization files are generated:
1. `crypto_price_trend.png`: A line graph tracking cryptocurrency price trends over time.
2. `crypto_market_cap_trend.png`: A line graph showing cryptocurrency market capitalization changes over time.

These visualizations are saved in the `data/` folder, and users can specify which cryptocurrencies they want to track when running the pipeline.

### Unit Testing

This project includes unit tests to ensure that each part of the pipeline (extraction, transformation, and loading) works correctly. To run the unit tests, use:
```bash
python -m unittest discover -s tests
```

---

### License

This project is licensed under the MIT License.

---

### Contact

If you have any questions or suggestions, feel free to reach out or open an issue!

---