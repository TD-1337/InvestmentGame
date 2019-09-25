from typing import Any


class Portfolio:
    from datetime import date
    from Order import Order
    from Stock import Stock

    def __init__(self, name):
        self.name = name
        self.orders = []

    def AddOrder(self, order):
        self.orders.append(order)

    def CalculateValueNow(self):
        value = 0
        for order in self.orders:
            value += order.volume * order.stock.retrieve_stock_price_now()
        return value

    def CalculateValueAtPurchaseDate(self):
        value = 0
        for order in self.orders:
            value += order.volume * order.price_at_purchase
        return value

    def CalculateReturn(self):
        valueAtPurchase = self.CalculateValueAtPurchaseDate()
        valueNow = self.CalculateValueNow()
        return valueNow - valueAtPurchase

