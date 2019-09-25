from typing import Any


class Portfolio:
    from datetime import date
    from Order import Order
    from Stock import Stock

    def __init__(self, name):
        self.Name = name
        self.Orders = []

    def add_order(self, order):
        self.Orders.append(order)

    def calculate_value_now(self):
        value = 0
        for order in self.Orders:
            value += order.Volume * order.Stock.retrieve_stock_price_now()
        return value

    def calculate_value_at_purchase_date(self):
        value = 0
        for order in self.Orders:
            value += order.Volume * order.PriceAtPurchase
        return value

    def calculate_return(self):
        value_at_purchase = self.calculate_value_at_purchase_date()
        value_now = self.calculate_value_now()
        return value_now - value_at_purchase

