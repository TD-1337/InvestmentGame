from datetime import datetime
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

            action_1 = input('What do you wish to do? (choose from: "Add Order", "Sell Order", "View Portfolio") ')
            number_of_existing_orders = sum([len(portfolio.orders) for portfolio in self.portfolio_dict.values()])

            if action_1.lower() == "view portfolio":
                # return portfolio
                portfolio_name = input("What is the name of the portfolio? ")
                self.print_portfolio(portfolio_name)

            elif action_1.lower() == "add order":
                # add order

                new_or_existing = input("Do you already have a portfolio with us? (Y/N) ")

                if new_or_existing.lower() == "n":
                    portfolio_name = input("What name do you wish to give your portfolio? ")
                    self.portfolio_dict[portfolio_name] = Portfolio(portfolio_name)
                    portfolio_this_order = self.portfolio_dict[portfolio_name]

                elif new_or_existing.lower() == "y":
                    portfolio_this_order = self.determine_portfolio()

                else:
                    raise Exception()

                new_order = self.create_buy_order(number_of_existing_orders, portfolio_this_order)
                portfolio_this_order.add_order(new_order)

                print('You bought ', new_order.volume, ' of ', new_order.stock.name, ' stocks, at EUR ',
                      new_order.price, ' at ', new_order.date, '. OrderID = ', new_order.order_id,
                      sep='')

            elif action_1.lower() == "sell order":
                portfolio_this_order = self.determine_portfolio()
                stock_balances = portfolio_this_order.calculate_balances()
                print("Please review your current open positions:")
                for key in stock_balances.keys():
                    print(key,":",stock_balances[key])
                new_order = self.create_sell_order(number_of_existing_orders, portfolio_this_order)
                portfolio_this_order.add_order(new_order)

                print('You sold ', float(new_order.volume) * -1, ' of ', new_order.stock.name, ' stocks, at EUR ',
                      new_order.price, ' at ', new_order.date, '. OrderID = ',
                      new_order.order_id,
                      sep='')

            else:
                print("Incorrect input, please try again")

            user_input = input('Do you wish to continue? (Y/N) ')

        print("Thanks for visiting!")

    def print_portfolio(self, portfolio_name):
        print_report_df = pd.DataFrame([x.return_as_dict() for x in self.portfolio_dict[portfolio_name].orders])
        print("Your portfolio consists of the following: ")
        print(print_report_df)  # Add optionality

    def create_buy_order(self, number_of_existing_orders, portfolio_this_order):
        stock_name = input("Which stock do you want to purchase? Please input ticker: ")
        volume = int(input("How many stocks do you want to purchase? "))
        date_of_purchase = datetime.now().strftime('%Y-%m-%d')
        stock = Stock(stock_name)
        stock_price_at_purchase = stock.retrieve_stock_price_now()
        order_id = number_of_existing_orders + 1
        new_order = Order(stock, volume, stock_price_at_purchase, date_of_purchase, order_id, portfolio_this_order.name)
        return new_order

    def create_sell_order(self, number_of_existing_orders, portfolio_this_order):
        stock_to_sell = input("Please indicate which stock (TICKER) you want to sell. ")
        amount_to_sell = float(input("Please indicate how much of " + stock_to_sell + " you want to sell. ")) * -1
        date_of_sale = datetime.now().strftime('%Y-%m-%d')
        stock = Stock(stock_to_sell)
        stock_price_at_sale = stock.retrieve_stock_price_now()
        order_id = number_of_existing_orders + 1
        new_order = Order(stock, amount_to_sell, stock_price_at_sale, date_of_sale, order_id,
                          portfolio_this_order.name)
        return new_order

    def determine_portfolio(self):
        portfolio_name = input("What is the name of the portfolio? ")
        portfolio_this_order = self.portfolio_dict[portfolio_name]
        return portfolio_this_order