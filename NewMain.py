from flask import Flask, escape, request, render_template, redirect
from pandas import pandas as pd
from .Order import Order
from .Stock import Stock
from .Portfolio import Portfolio
from datetime import datetime
from .Importer import Importer
from .PortfolioUtils import create_portfolio_this_order, create_buy_order, create_sell_order, determine_portfolio
from . import Exporter
import os

######################################
# Import existing order functionality
######################################

importer = Importer(os.getcwd())
portfolio_dict = importer.import_order_history_into_portfolios()


######################################
# Add new order / view portfolio via FLASK
######################################

app = Flask(__name__)
#app.run()

#Home Page
@app.route('/')
def usertype():
    return render_template("usertype.html")

#Add order page
@app.route('/buy_order', methods=['POST','GET'])
def buy_order():
    if request.method == "POST":

        number_of_existing_orders = sum([len(portfolio.orders) for portfolio in portfolio_dict.values()])

        # User input data
        portfolio_name = request.form['portfolio']
        stock = request.form['stock']
        amount = request.form['amount']
        next_action = request.form['next_action']

        #add order to dictionary
        portfolio_this_order = create_portfolio_this_order(portfolio_name, portfolio_dict)
        new_order = create_buy_order(stock, amount, number_of_existing_orders, portfolio_this_order)
        portfolio_this_order.add_order(new_order)

        #Next action
        if next_action =="No":
            Exporter.export_to_csv(portfolio_dict)
            return "Thank you for your business, you have purchased "+amount+" of "+stock+" stocks in portfolio "+portfolio_name
            # Export to CSV
        elif next_action =="Yes":
            return  render_template("buy_order.html")
        elif next_action =="Back to Home":
            Exporter.export_to_csv(portfolio_dict)
            return redirect("/")
    else:
        return render_template("buy_order.html")


#Sell order page
@app.route('/sell_order', methods=['POST','GET'])
def sell_order():
    if request.method == "POST":

        number_of_existing_orders = sum([len(portfolio.orders) for portfolio in portfolio_dict.values()])

        # User input data
        portfolio_name = request.form['portfolio']
        stock = request.form['stock']
        amount = request.form['amount']
        next_action = request.form['next_action']

        #add order to dictionary
        portfolio_this_order = determine_portfolio(portfolio_name, portfolio_dict)
        new_order = create_sell_order(stock,amount,number_of_existing_orders,portfolio_this_order)
        portfolio_this_order.add_order(new_order)

        #do something with this input
        if next_action =="No":
            Exporter.export_to_csv(portfolio_dict)
            return "Thank you for your business, you have sold "+amount+" of "+stock+" stocks in portfolio "+portfolio_name
            # Export to CSV
        elif next_action =="Yes":
            return  render_template("sell_order.html")
        elif next_action =="Back to Home":
            Exporter.export_to_csv(portfolio_dict)
            return redirect("/")
    else:
        return render_template("sell_order.html")

#Select Portfolio Page
@app.route('/select_portfolio', methods=['POST','GET'])
def select_and_view_portfolio():
    if request.method == "POST":
        #process user data
        portfolio_name = request.form['portfolio']
        portfolio_df = sub_portfolio(portfolio_name)

        return render_template("view_portfolio.html",  portfolio= portfolio_dict[portfolio_name])
    else:
        return render_template("select_portfolio.html")


def sub_portfolio(portfolio_name):
        print_report_df = pd.DataFrame([x.return_as_dict() for x in portfolio_dict[portfolio_name].orders])
        #print("Your portfolio consists of the following: ")
        #print(print_report_df)  # Add optionality
        return print_report_df


