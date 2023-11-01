import unittest
import pandas as pd


class TestDataQuality(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv("data/assets_data.csv")

    def test_completeness(self):
        missing_values = self.data.isnull().sum()
        self.assertEqual(missing_values.sum(), 0,
                         "There are missing values in the dataset.")

    def test_accuracy(self):
        acceptable_ranges = {
            "open": (0, 100000),
            "high": (0, 100000),
            "low": (0, 100000),
            "close": (0, 100000),
        }

        for column, (min_val, max_val) in acceptable_ranges.items():
            values = self.data[column]
            self.assertTrue(all(min_val <= values) and all(values <= max_val),
                            f"Values in {column} column are outside the"
                            " acceptable range."
                            )

    def test_consistency(self):
        duplicate_rows = self.data[self.data.duplicated()]
        self.assertTrue(duplicate_rows.empty, "Duplicate rows found in the"
                        " dataset."
                        )

    def test_validity(self):
        date_format_valid = pd.to_datetime(self.data.index, errors='coerce') \
            .notna().all()
        self.assertTrue(date_format_valid, "Date format is not valid.")

        symbol_columns = ["000001.SS", "AAPL", "CL=F", "GC=F", "HG=F",
                          "NVDA", "^DJI", "^GSPC", "^N100", "^N225"]
        valid_symbol_format = self.data[symbol_columns].notna()
        self.assertTrue(valid_symbol_format.all().all(), "Invalid symbol"
                        " format found.")


if __name__ == '__main__':
    unittest.main()
