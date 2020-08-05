import numpy as np
import pandas as pd
import ta

class Stock: 
    def __init__(self, ticker: str): # default constructor
        self.ticker = ticker
        self.indicators = {} # hash table of indicators
        self.price = 0
        self.last_updated = pd.to_datetime(0)

    def add_indicator(self, id: str, indicator: object):
        self.indicators[id] = indicator
    
    def update_indicators(self):
        # don't have access to a real-time library yet
        # when we do, we add data points to each Panda series
        pass


class Index:
    def __init__(self, name: str):
        self.name = name
        self.stocks = []
    
    def add_stock(self, stock: Stock):
        self.stocks.append(stock)

    def update_index(self):
        for pos in stocks:
            pos.update()


if __name__ == "__main__":
    msft = Stock("MSFT")
    # example of how we would process data
    high = pd.Series([127.36, 127.31, 127.21, 127.15, 127.08])
    low = pd.Series([126.36, 126.31, 126.21, 126.15, 126.08])
    close = pd.Series([127.0, 126.81, 127.11, 126.76, 127.08])
    volume = pd.Series([10,6,7,19,21])
    
    msft_vwap = ta.volume.volume_weighted_average_price(high, low, close, 5)
    msft.add_indicator("VWAP", msft_vwap)


