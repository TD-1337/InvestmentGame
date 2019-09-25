import matplotlib.pyplot as plt
from Stock import Stock
import pandas as pd
import datetime
import numpy as np

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

    def plot_portfolio_return(self, portfolio):
        # Retrieve stock history

        count_i_1 = 1
        for i in portfolio.orders:

            # Convert string to datetime
            date_time_action_date = datetime.datetime.strptime(i.date, "%Y-%m-%d")
            if count_i_1 == 1:
                min_date = date_time_action_date
                count_i_1 = 0
            else:
                min_date = min(min_date, date_time_action_date)

        for i in portfolio.orders:

            # Retrieve stock information
            stock = i.stock.name
            order_hist = Stock(stock).retrieve_stock_price_hist(min_date.strftime("%Y-%m-%d"))

            # Convert index to datetime and series to date frame
            order_hist.index = pd.to_datetime(order_hist.index)
            df_order_hist = pd.DataFrame({'Date': order_hist.index, 'Closing price': order_hist.values})

            # Add column for volumes
            date_time_action_date = datetime.datetime.strptime(i.date, "%Y-%m-%d")
            df_order_hist['Volume'] = df_order_hist['Date'].apply(
                lambda x: i.volume if x >= date_time_action_date else 0)

            # Calculate value by multiplying volume and price
            df_order_hist['Value'] = df_order_hist['Closing price'].multiply(df_order_hist['Volume'])

        # Plot
        plt.plot(sub_selection_series)
        plt.ylabel('Stock price')
        plt.title('Stockprice of ' + stock)
        plt.show()