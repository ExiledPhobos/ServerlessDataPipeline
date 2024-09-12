import unittest
from unittest.mock import patch, MagicMock
from lambdas.lambda_1_extract import lambda_1_extract

class TestLambda1Extract(unittest.TestCase):

    @patch('lambdas.lambda_1_extract.save_to_local_storage', autospec=True)  # Corrected patch path
    @patch('requests.get')
    def test_lambda_1_extract_success(self, mock_get, mock_save):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "name": "Bitcoin",
                "symbol": "btc",
                "current_price": 52725,
                "market_cap": 1043358522128,
                "last_updated": "2024-01-01"
            }
        ]
        mock_get.return_value = mock_response

        # Run the function
        result = lambda_1_extract()

        # Assert that save_to_local_storage was called once with the correct arguments
        mock_save.assert_called_once_with(data=mock_response.json.return_value, filename='crypto_raw.json')

    @patch('lambdas.lambda_1_extract.save_to_local_storage', autospec=True)  # Also mock save_to_local_storage for the fail test
    @patch('requests.get')
    def test_lambda_1_extract_fail(self, mock_get, mock_save):
        # Mock a failed API call
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        # Run the function
        result = lambda_1_extract()

        # Assert that the result is None (since a failed API call returns None)
        self.assertIsNone(result)

        # Assert that save_to_local_storage was not called
        mock_save.assert_not_called()

if __name__ == '__main__':
    unittest.main()