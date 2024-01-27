# Stock Visualization 

import matplotlib.pylot as plt
from alpha_vantage.timeseries import timeseries
import pandas as pd

API_KEY = 
symbol = 'AMZN'

def fetch_stock_data(api_key, symbol, interval='1d', output_size='compact'):
    """
    Fetch historical stock data from Alpha Vantage.
    :param api_key: Alpha Vantage API api_key
    :param symbol: Stock symbol
    :param interval: Data interval(default is '1d' for daily)
    """
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=symbol, outputsize=output_size)
    return data

def plot_stock_data(stock_data):
    """
    Plot stock data using Matplotlib.
    :param stock_data: Pandas DataFrame with stock data
    """
    plt.figure(figsize=(12,6))
    plt.plot(stock_data['4. close'], label='Closing Price', color='blue'),
    plt.title(f'Stock Price Overt Time - {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show


