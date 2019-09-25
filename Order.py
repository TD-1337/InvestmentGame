class Order:

    def __init__(self, stock, volume, price, date, order_id, portfolio):

        self.stock = stock
        self.volume = volume
        self.price = price
        self.date = date
        self.order_id = order_id
        self.portfolio = portfolio

    def return_as_dict(self):
        return {'Stock': self.stock.name, 'Volume': self.volume, 'Price': self.price,
                'Date': self.date, 'OrderId': self.order_id, 'Portfolio': self.portfolio}