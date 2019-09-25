from typing import Any
from datetime import datetime


class Portfolio:
    from datetime import date
    from .Order import Order
    from .Stock import Stock

    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_value_now(self):
        value = 0
        for order in self.orders:
            value += order.volume * order.stock.retrieve_stock_price_now()
        return value

    def calculate_value_at_purchase_date(self):
        value = 0
        for order in self.orders:
            value += order.volume * order.price_at_purchase
        return value

    def calculate_return(self):
        value_at_purchase = self.calculate_value_at_purchase_date()
        value_now = self.calculate_value_now()
        return value_now - value_at_purchase

    def calculate_balances(self, date = date.max):
        stock_balances = {}
        filtered_orders = filter_dictionary_on_dates(self.orders, date)
        for order in filtered_orders:
            stock_name = order.stock.name
            if not stock_name in stock_balances:
                stock_balances[stock_name] = order.volume
            else:
                stock_balances[stock_name] += order.volume
        return stock_balances

    def filter_dictionary_on_dates(dictObj, date):
        newDict = dict()
        # Iterate over all the items in dictionary
        for (key, value) in dictObj.items():
            # Check if item satisfies the given condition then add to new dict
            if (value.date <= date):
                newDict[key] = value
        return newDict
