import matplotlib.pyplot as plt
from Stock import Stock
import pandas as pd

class Visualise:

    def plot_stock_return(self, stock, start_date):
        # Retrieve stock history
        stock_returns = Stock(stock).retrieve_stock_price_hist("2018-09-25")

        # Index to datetime
        stock_returns.index = pd.to_datetime(stock_returns.index)

        print(len(stock_returns))

        # Get relevant time series
        sub_selection_series = stock_returns[stock_returns.index > start_date]

        # Plot
        plt.plot(sub_selection_series)
        plt.ylabel('Stock price')
        plt.title('Stockprice of ' + stock)
        plt.show()