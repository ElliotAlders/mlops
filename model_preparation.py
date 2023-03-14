from sklearn.linear_model import LinearRegression, ridge_regression
from data_preprocessing import x_train_scaled, y_train

model = LinearRegression(

)
model.fit(x_train_scaled, y_train)

score = model.score(x_train_scaled, y_train)
#print("Test score: {0:.2f} %".format(100 * score))