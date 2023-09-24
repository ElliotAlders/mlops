import pandas as pd

df = pd.read_csv("data/assets_data.csv", index_col=0)

# Feature engineering
for column in df.drop(columns='target').columns:
    df[f'{column}_ch'] = df[column] / df.shift(1)[column]

'''
import talib

# Moving Averages
df['SMA_20'] = talib.SMA(df['close'], timeperiod=20)
df['EMA_20'] = talib.EMA(df['close'], timeperiod=20)

# Technical Indicators
df['RSI'] = talib.RSI(df['close'], timeperiod=14)
df['MACD'], _, _ = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
df['bollinger_upper'], df['bollinger_middle'], df['bollinger_lower'] = talib.BBANDS(df['close'], timeperiod=20)

# Volatility Measures
df['ATR'] = talib.ATR(df['high'], df['low'], df['close'], timeperiod=14)
df['STD'] = df['close'].rolling(window=20).std()

# Volume-based Features
df['volume_SMA_20'] = talib.SMA(df['volume'], timeperiod=20)
df['volume_ratio'] = df['volume'] / df['volume'].rolling(window=20).mean()

'''


df.dropna(inplace=True)
df = df[df['target'] != 0]


from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

# Split into features (X) and target (y)
X = df.drop('target', axis=1)
y = df['target']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, index=X.index, columns=X.columns)

# Split into train and test sets
train_size = len(df) - 90  # Last 90 rows as the test set
X_train, X_test = X_scaled_df[:train_size], X_scaled_df[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Convert NumPy arrays back to DataFrames with feature names
X_train_df = pd.DataFrame(X_train, columns=X.columns)
X_test_df = pd.DataFrame(X_test, columns=X.columns)
y_train_df = pd.DataFrame(y_train, columns=['target'])  # Add a name to the target column
y_test_df = pd.DataFrame(y_test, columns=['target'])  # Add a name to the target column

# Save train and test DataFrames to CSV files with the date column as index
X_train_df.to_csv("data/train_features.csv", index=True)
X_test_df.to_csv("data/test_features.csv", index=True)
y_train_df.to_csv("data/train_target.csv", index=True)
y_test_df.to_csv("data/test_target.csv", index=True)


