import pandas as pd
from flask import Flask, render_template, request
import plotly.graph_objs as go

app = Flask(__name__, template_folder="templates")

# Load the data
assets_data = pd.read_csv("data/assets_data.csv", index_col=0)
train_predictions = pd.read_csv("data/train_prediction.csv", index_col=0)
test_predictions = pd.read_csv("data/test_prediction.csv", index_col=0)

predictions = pd.concat([train_predictions, test_predictions])

# Create a column for buy/sell signals
predictions['Signal'] = 'None'
predictions.loc[predictions['Prediction'] > 0, 'Signal'] = 'Buy'
predictions.loc[predictions['Prediction'] < 0, 'Signal'] = 'Sell'


@app.route('/', methods=['GET', 'POST'])
def plot():
    starting_value = 400  # Default starting value
    if request.method == 'POST':
        starting_value = float(request.form['starting_value'])

    # Calculate the value of the investment
    investment_value = []
    current_value = starting_value
    buy_dates = []
    sell_dates = []

    for date in assets_data.index:
        if date in predictions.index:
            signal = predictions.loc[date, 'Signal']

            if signal == 'Buy':
                buy_dates.append(date)
                price_change = assets_data.loc[date, 'target'] / 100
                current_value *= (1 + price_change)
            elif signal == 'Sell':
                sell_dates.append(date)
                pass

        investment_value.append(current_value)

    investment_data = pd.DataFrame(data=investment_value,
                                   index=assets_data.index,
                                   columns=['Investment Value'])

    table_data = pd.DataFrame({
        'Date': assets_data.index,
        'BTC Price': assets_data['close'],
        'Prediction': predictions['Prediction'],
        'Investment Value': investment_data['Investment Value']
    })

    fig = go.Figure()

    # Add the BTC Price line
    fig.add_trace(go.Scatter(
        x=assets_data.index,
        y=assets_data['close'],
        mode='lines',
        name='BTC Price'
        ))

    # Add the Investment Value line
    fig.add_trace(go.Scatter(
        x=investment_data.index,
        y=investment_data['Investment Value'],
        mode='lines',
        name='Investment Value'
        ))

    # Add Buy and Sell signals as markers
    fig.add_trace(go.Scatter(
        x=buy_dates,
        y=assets_data.loc[buy_dates, 'close'],
        mode='markers',
        name='Buy',
        marker_symbol='triangle-up',
        marker=dict(size=10, color='green')
        ))

    fig.add_trace(go.Scatter(
        x=sell_dates,
        y=assets_data.loc[sell_dates, 'close'],
        mode='markers',
        name='Sell',
        marker_symbol='triangle-down',
        marker=dict(size=10, color='red')
        ))

    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Value',
        title='BTC Price vs. Investment Value with Buy/Sell Signals',
    )

    plot_url = fig.to_html(full_html=False)

    return render_template('plot.html', plot_url=plot_url,
                           starting_value=starting_value, data=table_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
