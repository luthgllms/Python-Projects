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

