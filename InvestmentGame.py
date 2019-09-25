from Order import Order
from Stock import Stock
from Portfolio import Portfolio
from datetime import datetime
import pandas as pd
from Importer import Importer
from UserInterface import UserInterface
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

UserInterface(portfolio_dict).run_user_interface()

### View portfolio / returns
#new_portfolio.calculate_return()

### Sell (optional)

######################################
# Export new order functionality
######################################

# Get al orders and put them in a dataframe
for y in portfolio_dict:
    export_df = pd.DataFrame([x.return_as_dict() for x in portfolio_dict[y].orders])

time_stamp = datetime.now()

# Export the dataframe to a csv
export_df.to_csv('order.csv')

