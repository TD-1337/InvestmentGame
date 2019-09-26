from datetime import datetime
from .Order import Order
from .Stock import Stock
from .Portfolio import Portfolio

def create_portfolio_this_order(portfolio_name, portfolio_dict):
    if portfolio_name in portfolio_dict:
        portfolio_this_order = determine_portfolio(portfolio_name, portfolio_dict)
    else:
        portfolio_dict[portfolio_name] = Portfolio(portfolio_name)
        portfolio_this_order = portfolio_dict[portfolio_name]
    return portfolio_this_order

def create_buy_order(stockname, amount, number_of_existing_orders, portfolio_this_order):
    stock_name = stockname
    volume = amount
    date_of_purchase = datetime.now().strftime('%Y-%m-%d')
    stock = Stock(stock_name)
    stock_price_at_purchase = stock.retrieve_stock_price_now()
    order_id = number_of_existing_orders + 1
    new_order = Order(stock, volume, stock_price_at_purchase, date_of_purchase, order_id, portfolio_this_order.name)
    return new_order


def create_sell_order(stock, amount, number_of_existing_orders, portfolio_this_order):
    stock_to_sell = stock
    amount_to_sell = amount * -1
    date_of_sale = datetime.now().strftime('%Y-%m-%d')
    stock = Stock(stock_to_sell)
    stock_price_at_sale = stock.retrieve_stock_price_now()
    order_id = number_of_existing_orders + 1
    new_order = Order(stock, amount_to_sell, stock_price_at_sale, date_of_sale, order_id, portfolio_this_order.name)
    return new_order


def determine_portfolio(portfolio_name, portfolio_dict):
    portfolio_this_order = portfolio_dict[portfolio_name]
    return portfolio_this_order

