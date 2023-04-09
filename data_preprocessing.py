from sklearn.preprocessing import StandardScaler
from data_creation import x_train, y_train, x_test, y_test

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)

x_test_scaled = scaler.transform(x_test)