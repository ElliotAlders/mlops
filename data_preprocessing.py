import os
import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(input_file="data/assets_data.csv", data_dir="data"):

    os.makedirs(data_dir, exist_ok=True)

    df = pd.read_csv(input_file, index_col=0)

    # Additional features
    for column in df.drop(columns='target').columns:
        df[f'{column}_ch'] = df[column] / df.shift(1)[column]

    df.dropna(inplace=True)

    X = df.drop('target', axis=1)
    y = df['target']

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, index=X.index, columns=X.columns)

    # Train-test split
    train_size = len(df) - 90
    X_train, X_test = X_scaled_df[:train_size], X_scaled_df[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    X_train.to_csv(f"{data_dir}/train_features.csv", index=True)
    X_test.to_csv(f"{data_dir}/test_features.csv", index=True)
    y_train.to_csv(f"{data_dir}/train_target.csv", index=True)
    y_test.to_csv(f"{data_dir}/test_target.csv", index=True)


if __name__ == '__main__':
    preprocess_data()
