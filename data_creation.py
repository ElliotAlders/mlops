import yfinance as yf
import pandas as pd
import os


def create_data():

    os.makedirs("data", exist_ok=True)

    if os.path.exists("data/assets_data.csv"):
        print("Data file already exists. Skipping download.")
        return pd.read_csv("data/assets_data.csv",
                           index_col=0, parse_dates=True)

    btc_ticker = yf.Ticker("BTC-USD")

    df = btc_ticker.history(period="max")

    df.index = pd.to_datetime(df.index).date
    df.index = pd.to_datetime(df.index)

    del df["Dividends"]
    del df["Stock Splits"]

    df.columns = [c.lower() for c in df.columns]

    # Create target feature
    df['Tomorrow'] = df['close'].shift(-1)
    df['target'] = df['Tomorrow'].pct_change() * 100
    df = df.drop(['Tomorrow'], axis=1)

    assets = (
        "^GSPC ^DJI ^N225 ^N100 000001.SS "
        "CL=F GC=F HG=F NVDA AAPL"
    )

    additional_data = yf.download(assets, start="2014-09-17")

    df_add = additional_data.Close

    df_add = df_add.fillna(method='ffill')

    df_ = df.merge(df_add, left_index=True, right_index=True, how='left')

    df_ = df_.fillna(method='ffill')

    df_.dropna(inplace=True)

    df_.to_csv("data/assets_data.csv")

    return df_


if __name__ == '__main__':
    create_data()
