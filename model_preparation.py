from sklearn.svm import LinearSVR
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import pickle


def prepare_model(data_dir="data", model_name="linear_svr_model.pkl"):
    # Load training data
    X_train = pd.read_csv(f"{data_dir}/train_features.csv", index_col=0)
    y_train = pd.read_csv(f"{data_dir}/train_target.csv", index_col=0)

    print(X_train.shape)
    print(y_train.shape)

    model = LinearSVR(random_state=42, max_iter=10000)
    model.fit(X_train, y_train)
    predictions = model.predict(X_train)
    mse = mean_squared_error(y_train, predictions)
    r2 = r2_score(y_train, predictions)

    # Print evaluation metrics
    print("Training: ")
    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

    with open(model_name, "wb") as model_file:
        pickle.dump(model, model_file)


if __name__ == '__main__':
    prepare_model()
