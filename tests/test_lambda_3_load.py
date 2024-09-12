import unittest
from unittest.mock import patch, mock_open, MagicMock
from lambdas.lambda_3_load import lambda_3_load

class TestLambda3Load(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"name": "Bitcoin", "symbol": "btc", "current_price": 52725, "market_cap": 1043358522128, "last_updated": "2024-01-01"}]')
    @patch('csv.writer', autospec=True)  # Mock the CSV writer with autospec to capture arguments correctly
    def test_lambda_3_load(self, mock_csv_writer, mock_open_read):
        # Mock the CSV write operation separately
        mock_open_write = mock_open()

        # Set the mock for writing to CSV file
        mock_open_read.side_effect = [mock_open_read.return_value, mock_open_write()]

        # Run the function
        lambda_3_load()

        # Check if the JSON file was opened for reading
        mock_open_read.assert_any_call('./data/crypto_transformed.json', 'r')

        # Check if the CSV file was opened for appending
        mock_open_read.assert_any_call('./data/crypto_data.csv', 'a', newline='')

        # Assert that CSV writer was called with the correct file handle and dialect as a positional argument
        handle = mock_open_write()
        mock_csv_writer.assert_called_once_with(handle, 'excel')

if __name__ == '__main__':
    unittest.main()