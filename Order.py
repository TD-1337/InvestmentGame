class Order:

    def __init__(self, stock, volume, price_at_purchase, date_of_purchase, order_id, portfolio):

        self.stock = stock
        self.volume = volume
        self.price_at_purchase = price_at_purchase
        self.date_of_purchase = date_of_purchase
        self.order_id = order_id
        self.portfolio = portfolio

    def return_as_dict(self):
        return {'Stock': self.stock, 'Volume': self.volume, 'Price at purchase': self.price_at_purchase,
                'Date of purchase': self.date_of_purchase, 'OrderID': self.order_id, 'Portfolio': self.portfolio}