class Portfolio:
    def __init__(self, name, owner, orders):
        self.name = name
        self.owner = owner
        self.orders = []

    def AddOrder(self, order):
        self.orders.Append(order)
