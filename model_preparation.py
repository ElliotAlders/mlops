from sklearn.linear_model import LinearRegression
from data_preprocessing import x_train_scaled, y_train
import pickle

model = LinearRegression()

model.fit(x_train_scaled, y_train)

score = model.score(x_train_scaled, y_train)
print("Train score: {0:.2f} %".format(100 * score))

pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'wb') as file:
	pickle.dump(model, file)