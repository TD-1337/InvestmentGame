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

user_input = "n"

while user_input.lower() == "y":

    action_1 = input('What do you wish to do? (choose from: "Add Order", "View Portfolio") ')

    if action_1.lower() == "view portfolio":
        # return portfolio
        portfolio_name = input("What is the name of the portfolio? ")
        print_report_df = pd.DataFrame([x.return_as_dict() for x in portfolio_dict[portfolio_name].orders])

        print("Your portfolio consists of the following: ")
        print(print_report_df) # Add optionality

    elif action_1.lower() == "add order":
        # add order
        new_or_existing = input("Do you already have a portfolio with us? (Y/N) ")

        if new_or_existing.lower() == "n":
            portfolio_name = input("What name do you wish to give your portfolio? ")
            new_portfolio = Portfolio(portfolio_name)

        elif new_or_existing.lower() == "y":
            portfolio_name = input("What is the name of the portfolio? ")
            new_portfolio = Portfolio(portfolio_name)

        stock_name = input("Which stock do you want to purchase? Please input ticker: ")
        volume = int(input("How many stocks do you want to purchase? "))

        date_of_purchase = datetime.now().strftime('%Y-%m-%d')
        stock = Stock(stock_name)
        stock_price_at_purchase = stock.retrieve_stock_price_now()

        order_id = len(new_portfolio.orders) + 1
        new_order = Order(stock, volume, stock_price_at_purchase, date_of_purchase, order_id, new_portfolio.name)

        new_portfolio.add_order(new_order)
        portfolio_return = new_portfolio.calculate_return()

        print('You bought ', new_order.volume, ' of ', new_order.stock.name, ' stocks, at EUR ',
              new_order.price_at_purchase, ' at ', new_order.date_of_purchase, '. OrderID = ', new_order.order_id,
              sep='')

    else:
        print("Incorrect input, please try again")

    user_input = input('Do you wish to continue? (Y/N) ')

print("Thanks for visiting!")
######################################
# Export new order functionality
######################################

# Set var to check if dataframe needs to be created or appended
create_df = 1

# Get all orders and put them in a dataframe
for y in portfolio_dict:
    if create_df == 1:
        # Create data frame with first portfolio
        export_df = pd.DataFrame([x.return_as_dict() for x in portfolio_dict[y].orders])
        # Turn off creation of data frame
        create_df = 0
    else:
        # Append to data frame
        export_df = export_df.append(pd.DataFrame([x.return_as_dict() for x in portfolio_dict[y].orders]))


# Export the dataframe to a csv
export_df.to_csv('orders.csv')
