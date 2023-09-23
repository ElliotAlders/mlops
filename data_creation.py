import yfinance as yf
import os
import pandas as pd

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

additional_data = yf.download("^GSPC ^DJI ^N225 ^N100 000001.SS CL=F GC=F HG=F ETH-USD XRP-USD NVDA AAPL", start="2014-09-17")

df_add = additional_data.Close

df_add = df_add.fillna(method='ffill')

df_ = df.merge(df_add, left_index=True, right_index=True, how='left')

df_ = df_.fillna(method='ffill')

df_.to_csv("data/assets_data.csv")
