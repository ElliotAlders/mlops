import unittest
import os
import shutil
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from model_testing import test_model

class TestModelTesting(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.temp_dir = 'temp_test'
        os.mkdir(self.temp_dir)

        # Create temporary test data directory
        self.test_data_dir = os.path.join(self.temp_dir, 'data')
        os.mkdir(self.test_data_dir)

        # Create temporary test data with the required pattern
        test_features = pd.DataFrame({
            'open': [0.6094517778203015, 0.5752305624380339, 0.6419651434620808],
            'high': [0.6113455610433972, -0.7708091040664703, 0.13567440348198223],
            'low': [1.7675725883511366, 0.23635954562093095, 0.6465172737907839],
            'close': [1.0889859517616307, 0.4828933399370578, 2.657873561476418],
            'volume': [-0.10245559475336899, 1.173748536404144, 1.345324199328191]
        })

        test_target = pd.Series([1.6244525446594802, 2.223711856284328, 0.06420914380936726], name='target')

        test_features.to_csv(os.path.join(self.test_data_dir, 'test_features.csv'), index=True)
        test_target.to_csv(os.path.join(self.test_data_dir, 'test_target.csv'), index=True)

        # Create a simple linear regression model and save it to a pickle file
        model = LinearRegression()
        model.fit(test_features, test_target)
        with open(os.path.join(self.temp_dir, 'linear_regression_model.pkl'), 'wb') as model_file:
            pickle.dump(model, model_file)

    def tearDown(self):
        # Clean up temporary directory and files
        shutil.rmtree(self.temp_dir)

    def test_test_model(self):
        # Call the function with the temporary directory and model path
        result = test_model(model_path=os.path.join(self.temp_dir, 'linear_regression_model.pkl'),
                            data_dir=self.test_data_dir)

        # Assert that the result is as expected
        self.assertTrue("Mean Squared Error:" in result)
        self.assertTrue("R-squared:" in result)

if __name__ == '__main__':
    unittest.main()
