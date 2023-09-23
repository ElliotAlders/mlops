import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

# Load the saved model from the file
with open("linear_svr_model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)

X_test = pd.read_csv("data/test_features.csv", index_col=0)
y_test = pd.read_csv("data/test_target.csv", index_col=0)

# Use the loaded model to make predictions
predictions = loaded_model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Print evaluation metrics
print("Mean Squared Error:", mse)
print("R-squared:", r2)
