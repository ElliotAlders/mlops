import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import io
import base64

app = Flask(__name__, template_folder="templates")

# Load the data
assets_data = pd.read_csv("data/assets_data.csv", index_col=0)
train_predictions = pd.read_csv("data/train_prediction.csv", index_col=0)
test_predictions = pd.read_csv("data/test_prediction.csv", index_col=0)

# Combine train and test predictions into one DataFrame
predictions = pd.concat([train_predictions, test_predictions])

# Create a column for buy/sell signals
predictions['Signal'] = 'None'
predictions.loc[predictions['Prediction'] > 0, 'Signal'] = 'Buy'
predictions.loc[predictions['Prediction'] < 0, 'Signal'] = 'Sell'

@app.route('/', methods=['GET', 'POST'])
def plot():
    starting_value = 100  # Default starting value
    if request.method == 'POST':
        starting_value = float(request.form['starting_value'])

    # Calculate the value of the investment
    investment_value = []
    current_value = starting_value  # Starting value set by the user
    buy_dates = []
    sell_dates = []

    for date in assets_data.index:
        if date in predictions.index:
            close_price = assets_data.loc[date, 'close']
            signal = predictions.loc[date, 'Signal']

            if signal == 'Buy':
                buy_dates.append(date)
                price_change = assets_data.loc[date, 'target'] / 100
                current_value *= (1 + price_change)
            elif signal == 'Sell':
                sell_dates.append(date)
                pass

        investment_value.append(current_value)

    investment_data = pd.DataFrame(data=investment_value, index=assets_data.index,
                                   columns=['Investment Value'])

    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(assets_data.index, assets_data['close'], label="BTC Price",
             color='blue', zorder=2)
    plt.plot(investment_data.index, investment_data['Investment Value'],
             label="Investment Value", color='yellow', zorder=2)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("BTC Price vs. Investment Value with Buy/Sell Signals")
    plt.legend()
    plt.grid(True)

    # Add Buy and Sell signal markers
    plt.scatter(buy_dates, assets_data.loc[buy_dates, 'close'], label="Buy",
                color='green', marker='^', s=5, zorder=2)
    plt.scatter(sell_dates, assets_data.loc[sell_dates, 'close'], label="Sell",
                color='red', marker='v', s=5, zorder=2)

    # Convert the Matplotlib plot to a base64 encoded PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('plot.html', plot_url=plot_url, starting_value=starting_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
