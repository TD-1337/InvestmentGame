from typing import Any


class Portfolio:
    from datetime import date
    from Order import Order
    from Stock import Stock

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.orders = []

    def AddOrder(self, order):
        self.orders.append(order)

    def CalculateValue(self):
        value = 0
        for order in self.orders:
            value += order.Volume * order.Stock.retrieve_stock_price_now()
        return value

    def ValueAtPurchaseDate(self):
        value = 0
        for order in self.orders:
            value += order.Volume * order.PriceAtPurchase
        return value