from sklearn.svm import LinearSVR
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import pickle

X_train = pd.read_csv("data/train_features.csv", index_col=0)
y_train = pd.read_csv("data/train_target.csv", index_col=0)

print(X_train.shape)
print(y_train.shape)

# Train your model and evaluate its performance
model = LinearSVR(random_state=42, max_iter=10000)
model.fit(X_train, y_train)
predictions = model.predict(X_train)
mse = mean_squared_error(y_train, predictions)
r2 = r2_score(y_train, predictions)

# Print evaluation metrics
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Save the trained model to a file using pickle
with open("linear_svr_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
