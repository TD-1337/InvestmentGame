from flask import Flask, escape, request, render_template, redirect

from .Order import Order
from .Stock import Stock
from .Portfolio import Portfolio
from datetime import datetime
from .Importer import Importer
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


#Home Page
@app.route('/')
def usertype():
    return render_template("usertype.html")

#Add order page
@app.route('/add_order', methods=['POST','GET'])
def add_order():
    if request.method == "POST":
        #User input data
        portfolio = request.form['portfolio']
        stock= request.form['stock']
        amount = request.form['amount']
        next_action = request.form['next_action']
        if portfolio in portfolio_dict:
            portfolio_this_order = determine_portfolio(portfolio)
        else:
            portfolio_dict[portfolio] = Portfolio(portfolio)
            portfolio_this_order = portfolio_dict[portfolio]

        #add order to dictionary
        number_of_existing_orders = sum([len(portfolio.orders) for portfolio in portfolio_dict.values()])
        create_buy_order(stock, amount, number_of_existing_orders, portfolio_this_order)
        portfolio_this_order.add_order(new_order)

        #Next action
        if next_action =="No":
            return "Thank you for your business, you have purchased "+volume+" of "+stock_name+" stocks in portfolio "+portfolio_name
            # Export to CSV
            Exporter.export_to_csv(portfolio_dict)
        elif next_action =="Yes":
            return  render_template("add_order.html")
        elif next_action =="Back to Home":
            return redirect("/")
    else:
        return render_template("add_order.html")

#Sell order page
@app.route('/sell_order', methods=['POST','GET'])
def sell_order():
    if request.method == "POST":
        #process user data
        portfolio_name = request.form['portfolio']
        stock_name = request.form['stock']
        volume = request.form['amount']
        next_action = request.form['next_action']
        portfolio_this_order = portfolio_dict[portfolio_name]

        #do something with this input
        if next_action =="No":
            return "Thank you for your business, you have sold "+volume+" of "+stock_name+" stocks in portfolio "+portfolio_name
            # Export to CSV
            Exporter.export_to_csv(portfolio_dict)
        elif next_action =="Yes":
            return  render_template("sell_order.html")
        elif next_action =="Back to Home":
            return redirect("/")
    else:
        return render_template("sell_order.html")

#View Portfolio Page
@app.route('/view_portfolio', methods=['POST','GET'])
def form():
    if request.method == "POST":
        #process user data
        portfolio = request.form['portfolio']
        return "thank you for your business"+portfolio
    else:
        return render_template("view_portfolio.html")





def create_buy_order(self, stockname, amount, number_of_existing_orders, portfolio_this_order):
        stock_name = stockname
        volume = amount
        date_of_purchase = datetime.now().strftime('%Y-%m-%d')
        stock = Stock(stock_name)
        stock_price_at_purchase = stock.retrieve_stock_price_now()
        order_id = number_of_existing_orders + 1
        new_order = Order(stock, volume, stock_price_at_purchase, date_of_purchase, order_id, portfolio_this_order.name)
        return new_order

def create_sell_order(self, stock, amount, number_of_existing_orders, portfolio_this_order):
        stock_to_sell = stock
        amount_to_sell = amount
        date_of_sale = datetime.now().strftime('%Y-%m-%d')
        stock = Stock(stock_to_sell)
        stock_price_at_sale = stock.retrieve_stock_price_now()
        order_id = number_of_existing_orders + 1
        new_order = Order(stock, amount_to_sell, stock_price_at_sale, date_of_sale, order_id,
                          portfolio_this_order.name)
        return new_order

def determine_portfolio(self, portfolio):
        portfolio_name = portfolio
        portfolio_this_order = self.portfolio_dict[portfolio_name]
        return portfolio_this_order


