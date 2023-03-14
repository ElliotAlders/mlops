from model_preparation import model
from data_preprocessing import x_test_scaled, y_test

score = model.score(x_test_scaled, y_test)

print("Test score: {0:.2f} %".format(100 * score))