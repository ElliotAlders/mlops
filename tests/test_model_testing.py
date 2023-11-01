import unittest
import os
import shutil
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from model_testing import test_model


class TestModelTesting(unittest.TestCase):
    def setUp(self):
        self.temp_dir = 'temp_test'
        os.mkdir(self.temp_dir)

        self.test_data_dir = os.path.join(self.temp_dir, 'data')
        os.mkdir(self.test_data_dir)

        test_features = pd.DataFrame({
            'open': [0.6095, 0.5759, 0.6418],
            'high': [0.6112, -0.7703, 0.13523],
            'low': [1.7676, 0.23695, 0.6469],
            'close': [1.0887, 0.4828, 2.657],
            'volume': [-0.10299, 1.173, 1.345]
        })

        test_target = pd.Series([1.624, 2.223, 0.064], name='target')

        test_features.to_csv(os.path.join(self.test_data_dir,
                                          'test_features.csv'), index=True)
        test_target.to_csv(os.path.join(self.test_data_dir, 'test_target.csv'),
                           index=True)

        model = LinearRegression()
        model.fit(test_features, test_target)
        with open(os.path.join(self.temp_dir,
                               'test_model.pkl'), 'wb') as model_file:
            pickle.dump(model, model_file)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_test_model(self):
        result = test_model(model_path=os.path.join(self.temp_dir,
                                                    'test_model.pkl'),
                            data_dir=self.test_data_dir)

        self.assertTrue("Mean Squared Error:" in result)
        self.assertTrue("R-squared:" in result)


if __name__ == '__main__':
    unittest.main()
