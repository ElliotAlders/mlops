from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

data = load_diabetes()

x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=5)