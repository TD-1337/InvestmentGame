class Portfolio:
    from datetime import date
    import Order

    def __init__(self, name, owner, orders):
        self.name = name
        self.owner = owner
        self.orders = []

    def AddOrder(self, order):
        self.orders.Append(order)

    def CalculateValue(self, orders):
        for order in orders:
            value += order.volume * order.stock.price(date.today())

    def ValueAtPurchaseDate(self, orders):
        for order in orders:
            value += order.volume * order.stock.price(Order.DateOfPurchase)