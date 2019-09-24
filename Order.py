class Order:

    def __init__(self, stock, volume, dateOfPurchase, orderId):

        self.Stock = stock
        self.Volume = volume
        self.DateOfPurchase = dateOfPurchase
        self.OrderId = orderId

        print('You bought ', self.Volume, ' number of ', self.Stock, ' stocks, at ', self.DateOfPurchase, '. OrderID= ',
              self.OrderId, sep='')
