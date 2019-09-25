from Order import Order
from Stock import Stock
from Portfolio import Portfolio
from datetime import datetime
import pandas as pd
from Importer import Importer
from UserInterface import UserInterface
import Exporter
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

#Export to CSV
Exporter.export_to_csv(portfolio_dict)
