import pandas as pd
from .Order import Order
from .Stock import Stock
from .Portfolio import Portfolio

class Importer:
    def __init__(self, working_directory):
        self.working_directory = working_directory

    def import_order_history_into_portfolios(self):
        order_history = pd.read_csv("orders.csv")
        portfolio_dict = {}

        for index, row in order_history.iterrows():
            stock_this_order = Stock(row['Stock'])
            volume_this_order = row['Volume']
            price_this_order = row['Price']
            date_this_order = row['Date']
            order_id_this_order = row['OrderId']
            portfolio_this_order = row['Portfolio']
            new_order = Order(stock_this_order, volume_this_order, price_this_order, date_this_order, order_id_this_order, portfolio_this_order)

            # Check if portfolio name already exists in dictionary
            if not portfolio_this_order in portfolio_dict:
                new_portfolio = Portfolio(portfolio_this_order)
                new_portfolio.add_order(new_order)
                portfolio_dict[portfolio_this_order] = new_portfolio
            else:
                portfolio_dict[portfolio_this_order].add_order(new_order)

        return portfolio_dict