import datetime
from Order import Order
from Stock import Stock
from Portfolio import Portfolio
import pandas as pd

class UserInterface:

    def __init__(self, portfolio_dict):
        self.portfolio_dict = portfolio_dict

    def run_user_interface(self):
        user_input = "y"

        while user_input.lower() == "y":

            action_1 = input('What do you wish to do? (choose from: "Add Order", "View Portfolio") ')

            if action_1.lower() == "view portfolio":
                # return portfolio
                portfolio_name = input("What is the name of the portfolio? ")
                print_report_df = pd.DataFrame([x.return_as_dict() for x in self.portfolio_dict[portfolio_name].orders])

                print("Your portfolio consists of the following: ")
                print(print_report_df)  # Add optionality

            elif action_1.lower() == "add order":
                # add order

                number_of_existing_orders = sum([len(portfolio.orders) for portfolio in self.portfolio_dict.values()])

                new_or_existing = input("Do you already have a portfolio with us? (Y/N) ")

                if new_or_existing.lower() == "n":
                    portfolio_name = input("What name do you wish to give your portfolio? ")
                    self.portfolio_dict[portfolio_name] = Portfolio(portfolio_name)
                    portfolio_this_order = self.portfolio_dict[portfolio_name]

                elif new_or_existing.lower() == "y":
                    portfolio_name = input("What is the name of the portfolio? ")
                    portfolio_this_order = self.portfolio_dict[portfolio_name]

                else:
                    raise Exception()

                stock_name = input("Which stock do you want to purchase? Please input ticker: ")
                volume = int(input("How many stocks do you want to purchase? "))
                date_of_purchase = datetime.now().strftime('%Y-%m-%d')
                stock = Stock(stock_name)
                stock_price_at_purchase = stock.retrieve_stock_price_now()

                order_id = number_of_existing_orders + 1
                new_order = Order(stock, volume, stock_price_at_purchase, date_of_purchase, order_id, portfolio_this_order.name)

                portfolio_this_order.add_order(new_order)

                print('You bought ', new_order.volume, ' of ', new_order.stock.name, ' stocks, at EUR ',
                      new_order.price_at_purchase, ' at ', new_order.date_of_purchase, '. OrderID = ', new_order.order_id,
                      sep='')

            else:
                print("Incorrect input, please try again")

            user_input = input('Do you wish to continue? (Y/N) ')

        print("Thanks for visiting!")