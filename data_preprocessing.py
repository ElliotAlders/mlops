from sklearn.preprocessing import StandardScaler
from data_creation import x_train, y_train, x_test, y_test

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
#print(scaler.mean_, scaler.scale_)

x_test_scaled = scaler.fit_transform(x_test)
#print(scaler.mean_, scaler.scale_)

#print(x_train_scaled.mean(axis=0), x_test_scaled.mean(axis=0))
