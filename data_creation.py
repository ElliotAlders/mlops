from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data = load_diabetes()

df = pd.DataFrame(data=np.c_[data['data'], data['target']], columns=data['feature_names']+['target'])
#print(df)

x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=5)