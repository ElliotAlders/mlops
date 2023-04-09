from data_preprocessing import x_test_scaled, y_test
from model_preparation import pkl_filename, pickle

with open(pkl_filename, 'rb') as file:
	pickle_model = pickle.load(file)

score = pickle_model.score(x_test_scaled, y_test)

print("Test score: {0:.2f} %".format(100 * score))
Ypredict = pickle_model.predict(x_test_scaled)