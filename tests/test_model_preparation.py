import unittest
import pandas as pd
import os
from model_preparation import prepare_model


class TestModelPreparation(unittest.TestCase):
    def setUp(self):
        # Create temporary test data
        self.test_data_dir = "test_data"
        os.makedirs(self.test_data_dir, exist_ok=True)

        # Create sample training features and target CSV files
        self.X_train = pd.DataFrame({'feature1': [1, 2, 3],
                                     'feature2': [4, 5, 6]})
        self.y_train = pd.Series([10, 20, 30])
        self.X_train.to_csv(os.path.join(self.test_data_dir,
                                         "train_features.csv"), index=True)
        self.y_train.to_csv(os.path.join(self.test_data_dir,
                                         "train_target.csv"), index=True)

    def tearDown(self):
        # Clean up temporary test data
        os.remove(os.path.join(self.test_data_dir, "train_features.csv"))
        os.remove(os.path.join(self.test_data_dir, "train_target.csv"))
        os.rmdir(self.test_data_dir)

    def test_prepare_model(self):
        # Run the model preparation function
        prepare_model(data_dir=self.test_data_dir,
                      model_name="test_linear_svr_model.pkl")

        # Check if the model file is created
        self.assertTrue(os.path.exists("test_linear_svr_model.pkl"))


if __name__ == '__main__':
    unittest.main()
