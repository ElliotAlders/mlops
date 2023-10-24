import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score


def test_model(model_path="linear_svr_model.pkl", data_dir="data"):

    with open(model_path, "rb") as model_file:
        loaded_model = pickle.load(model_file)

    X_test = pd.read_csv(f"{data_dir}/test_features.csv", index_col=0)
    y_test = pd.read_csv(f"{data_dir}/test_target.csv", index_col=0)

    predictions = loaded_model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    result = f"Mean Squared Error: {mse}\nR-squared: {r2}"

    print("Testing: ")
    print(result)

    predictions_df = pd.DataFrame(predictions, index=X_test.index,
                                  columns=["Prediction"])
    predictions_df.to_csv(f"{data_dir}/test_prediction.csv", index=True)

    return result


if __name__ == '__main__':
    test_model()
