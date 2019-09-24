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
        for order in self.orders:
            value += order.Volume * order.Stock.retrieve_stock_price_now()

    def ValueAtPurchaseDate(self):
        for order in self.orders:
            value += order.Volume * order.PriceAtPurchase