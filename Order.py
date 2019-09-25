class Order:

    def __init__(self, stock, volume, priceAtPurchase, dateOfPurchase, orderId, portfolio):

        self.Stock = stock
        self.Volume = volume
        self.PriceAtPurchase = priceAtPurchase
        self.DateOfPurchase = dateOfPurchase
        self.OrderId = orderId
        self.Portfolio = portfolio

    def return_as_dict(self):
        return {'Stock': self.Stock, 'Volume': self.Volume, 'Price at purchase': self.priceAtPurchase,
                'Date of purchase': self.DateOfPurchase, 'OrderID': self.OrderId, 'Portfolio': self.Portfolio}