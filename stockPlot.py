# Stock Visualization 

import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

API_KEY = 'TE7TY30VEWVGWQ64' # Personal Alpha Vantage API Key
symbol = 'AMZN' # Stock symbol

def fetch_stock_data(api_key, symbol, interval='1d', output_size='compact'):
    """
    Fetch historical stock data from Alpha Vantage.
    :param api_key: Alpha Vantage API api_key
    :param symbol: Stock symbol
    :param interval: Data interval(default is '1d' for daily)
    :param output_size: Output size ('compact' for 100 data points, 'full' for all)
    return: Pandas DataFrame with stock data
    """
    ts = TimeSeries(key=api_key, output_format='pandas')
    # Get Daily Stock Data
    data, meta_data = ts.get_daily(symbol=symbol, outputsize=output_size)
    return data

def plot_stock_data(stock_data):
    """
    Plot stock data using Matplotlib.
    :param stock_data: Pandas DataFrame with stock data
    """
    # Plot closing prices over time
    plt.figure(figsize=(12,6))
    plt.plot(stock_data['4. close'], label='Closing Price', color='blue')

    # Labels, title, legend and grid
    plt.title(f'Stock Price Over Time - {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Fetch stock data using API key and symbol
    stock_data = fetch_stock_data(API_KEY, symbol)

    #Plot the fetched stock data
    plot_stock_data(stock_data)

if __name__ == "__main__":  

    #Execute the main function if the scrpt is run directly
    main()



