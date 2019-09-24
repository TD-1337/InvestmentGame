from typing import Any


class Portfolio:
    from datetime import date
    from Order import Order
    from Stock import Stock

    def __init__(self, name, owner):
        self.Name = name
        self.Owner = owner
        self.Orders = []

    def AddOrder(self, order):
        self.Orders.append(order)

    def CalculateValueNow(self):
        value = 0
        for order in self.Orders:
            value += order.Volume * order.Stock.retrieve_stock_price_now()
        return value

    def CalculateValueAtPurchaseDate(self):
        value = 0
        for order in self.Orders:
            value += order.Volume * order.PriceAtPurchase
        return value

    def CalculateReturn(self):
        valueAtPurchase = self.CalculateValueAtPurchaseDate()
        valueNow = self.CalculateValueNow()
        return valueNow - valueAtPurchase

