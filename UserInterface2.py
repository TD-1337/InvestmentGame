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

@app.route('/')
def usertype():
    return render_template("usertype.html")

@app.route('/add_order', methods=['POST','GET'])
def add_order():
    if request.method == "POST":
        #process user data
        portfolio_name = request.form['portfolio']
        stock_name = request.form['stock']
        amount = request.form['amount']
        next_action = request.form['next_action']
        portfolio_this_order = portfolio_dict[portfolio_name]
        # date_of_purchase = datetime.now().strftime('%Y-%m-%d')
        # stock = Stock(stock_name)
        # stock_price_at_purchase = stock.retrieve_stock_price_now()
        # number_of_existing_orders = sum([len(portfolio.orders) for portfolio in portfolio_dict.values()])
        # order_id = number_of_existing_orders + 1
        # new_order = Order(stock, volume, stock_price_at_purchase, date_of_purchase, order_id, portfolio_this_order.name)
        # portfolio_this_order.add_order(new_order)

        #do something with this input
        if next_action =="No":
            return "Thank you for your business, you have purchased "+amount+" of "+stock_name+" stocks in portfolio "+portfolio_name
            # Export to CSV
            Exporter.export_to_csv(portfolio_dict)
        elif next_action =="Yes":
            return  render_template("add_order.html")
        elif next_action =="Back to Home":
            return redirect("/")
    else:
        return render_template("add_order.html")

@app.route('/view_portfolio', methods=['POST','GET'])
def form():
    if request.method == "POST":
        #process user data
        portfolio = request.form['portfolio']
        return "thank you for your business"+portfolio
    else:
        return render_template("view_portfolio.html")