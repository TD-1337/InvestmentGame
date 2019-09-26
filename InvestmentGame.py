from Order import Order
from Stock import Stock
from Portfolio import Portfolio
from datetime import datetime
from Importer import Importer
from UserInterface import UserInterface
import Exporter
import os
from Visualise import Visualise
from Stock import Stock

######################################
# Import existing order functionality
######################################

importer = Importer(os.getcwd())
portfolio_dict = importer.import_order_history_into_portfolios()

### import class which imports content of csv to Portfolio / Order objects

######################################
# Visualise test
######################################
# 
visualisation = Visualise()
#visualisation.plot_stock_return("TWTR", '25-09-2018')

visualisation.plot_portfolio_return(portfolio_dict['PortfolioStef'], 'Plaatje.png')

######################################
# Add new order
######################################

# UserInterface(portfolio_dict).run_user_interface()

### View portfolio / returns
#new_portfolio.calculate_return()
### Sell (optional)


######################################
# Export new order functionality
######################################

# Export to CSV
Exporter.export_to_csv(portfolio_dict)
