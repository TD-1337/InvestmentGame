class Order:

    def __init__(self, stock, volume, priceAtPurchase, dateOfPurchase, orderId, portfolio):

        self.Stock = stock
        self.Volume = volume
        self.PriceAtPurchase = priceAtPurchase
        self.DateOfPurchase = dateOfPurchase
        self.OrderId = orderId
        self.Portfolio = portfolio

        print('You bought ', self.Volume, ' number of ', self.Stock, ' stocks, at ', self.DateOfPurchase, '. OrderID= ',
              self.OrderId, sep='')
