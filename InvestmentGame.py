from Order import Order
from Stock import Stock
from Portfolio import Portfolio
from datetime import datetime
import pandas as pd
from Importer import Importer
import os

######################################
# Import existing order functionality
######################################

importer = Importer(os.getcwd())
portfolio_dict = importer.import_order_history_into_portfolios()

### import class which imports content of csv to Portfolio / Order objects

######################################
# Add new order
######################################

# Ask user what he/she wants to do

### Add order or multiple orders
### View portfolio / returns
### Sell (optional)


portfolio_name = "My Portfolio"

new_portfolio = Portfolio(portfolio_name, owner_name)

stock_name = input("Which stock do you want to purchase? Please input ticker ")
volume = int(input("How many stocks do you want to purchase? "))

date_of_purchase = datetime.now().strftime('%Y-%m-%d')

stock = Stock(stock_name)
stock_price_at_purchase = stock.retrieve_stock_price_now()

order_id = len(new_portfolio.orders) + 1
new_order = Order(stock, volume, stock_price_at_purchase, date_of_purchase, order_id, new_portfolio.Name)

new_portfolio.addorder(new_order)
portfolio_return = new_portfolio.calculate_return()

######################################
# Export new order functionality
######################################

# Get al orders and put them in a dataframe
export_df = pd.DataFrame([x.return_as_dict() for x in order_list])

# Export the dataframe to a csv
export_df.to_csv('order.csv')

