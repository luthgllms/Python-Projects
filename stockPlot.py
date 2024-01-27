# Stock Visualization 

import matplotlib.pylot as plt
from alpha_vantage.timeseries import timeseries
import pandas as pd

API_KEY = 
symbol = 'AMZN'

def fetch_stock_data(api_key, sym)