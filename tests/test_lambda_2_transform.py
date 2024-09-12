import unittest
from unittest.mock import patch, mock_open
from lambdas.lambda_2_transform import lambda_2_transform

class TestLambda2Transform(unittest.TestCase):

    @patch('lambdas.lambda_2_transform.save_to_local_storage', autospec=True)  # Correct patch path
    @patch('builtins.open', new_callable=mock_open, read_data='[{"name": "Bitcoin", "symbol": "btc", "current_price": 52725, "market_cap": 1043358522128, "price_change_percentage_24h": 0.5, "circulating_supply": 21000000, "last_updated": "2024-01-01"}]')
    def test_lambda_2_transform(self, mock_file, mock_save):
        # Run the function
        transformed_data = lambda_2_transform()

        # Assert that save_to_local_storage was called once with the correct transformed data
        self.assertIsNotNone(transformed_data)
        mock_save.assert_called_once_with(data=transformed_data, filename='crypto_transformed.json')

if __name__ == '__main__':
    unittest.main()