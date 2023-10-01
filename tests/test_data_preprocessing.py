import unittest
import pandas as pd
import os

from data_preprocessing import preprocess_data

class TestDataPreprocessing(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_data"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Clean up the temporary directory
        if os.path.exists(self.test_dir):
            for file in os.listdir(self.test_dir):
                file_path = os.path.join(self.test_dir, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            os.rmdir(self.test_dir)

    def test_preprocess_data(self):
        # Create a sample CSV file for testing
        sample_data = {
            'open': [100, 101, 102, 103, 104],
            'high': [105, 106, 107, 108, 109],
            'low': [95, 96, 97, 98, 99],
            'close': [101, 102, 103, 104, 105],
            'volume': [1000, 1100, 1200, 1300, 1400],
            'target': [1.0, 2.0, 1.5, -1.0, 0.5]
        }
        df = pd.DataFrame(sample_data)
        csv_file = os.path.join(self.test_dir, "sample_data.csv")
        df.to_csv(csv_file, index=False)

        # Call the preprocess_data function on the sample data
        preprocess_data(csv_file, self.test_dir)

        # Check if the expected output CSV files exist
        expected_files = [
            "train_features.csv",
            "test_features.csv",
            "train_target.csv",
            "test_target.csv"
        ]

        for file in expected_files:
            file_path = os.path.join(self.test_dir, file)
            self.assertTrue(os.path.exists(file_path))

if __name__ == '__main__':
    unittest.main()
