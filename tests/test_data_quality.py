import unittest
import pandas as pd


class TestDataQuality(unittest.TestCase):
    def setUp(self):
        # Load your data here
        self.data = pd.read_csv("data/assets_data.csv")

    def test_completeness(self):
        # Check for missing values
        missing_values = self.data.isnull().sum()
        self.assertEqual(missing_values.sum(), 0,
                         "There are missing values in the dataset.")

    def test_accuracy(self):
        # Define acceptable ranges for numerical columns
        acceptable_ranges = {
            "open": (0, 100000),
            "high": (0, 100000),
            "low": (0, 100000),
            "close": (0, 100000),
        }

        # Check if values are within acceptable ranges
        for column, (min_val, max_val) in acceptable_ranges.items():
            values = self.data[column]
            self.assertTrue(all(min_val <= values) and all(values <= max_val),
                            f"Values in {column} column are outside the"
                            " acceptable range."
                            )

    def test_consistency(self):
        # Check for duplicate rows
        duplicate_rows = self.data[self.data.duplicated()]
        self.assertTrue(duplicate_rows.empty, "Duplicate rows found in the"
                        " dataset."
                        )

    def test_validity(self):
        # Check date format validity
        date_format_valid = pd.to_datetime(self.data.index, errors='coerce') \
            .notna().all()
        self.assertTrue(date_format_valid, "Date format is not valid.")

        # Check format validity for specific columns (e.g., symbols)
        symbol_columns = ["000001.SS", "AAPL", "CL=F", "GC=F", "HG=F",
                          "NVDA", "^DJI", "^GSPC", "^N100", "^N225"]
        valid_symbol_format = self.data[symbol_columns].notna()
        self.assertTrue(valid_symbol_format.all().all(), "Invalid symbol"
                        " format found.")


if __name__ == '__main__':
    unittest.main()
