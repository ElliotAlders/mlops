import unittest
import pandas as pd
from data_creation import create_data

class TestDataCreation(unittest.TestCase):
    def test_process_data(self):

        result_df = create_data()
        
        self.assertFalse(result_df.empty)

        expected_columns = ['open', 'high', 'low', 'close', 'volume', 'target', '000001.SS','AAPL','CL=F','ETH-USD','GC=F','HG=F','NVDA','XRP-USD','^DJI','^GSPC','^N100','^N225']

        for col in expected_columns:
            self.assertIn(col, result_df.columns)

        self.assertGreater(len(result_df), 3000)

if __name__ == '__main__':
    unittest.main()
