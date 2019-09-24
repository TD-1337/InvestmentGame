from Order import Order
from Stock import Stock
from Portfolio import Portfolio
from datetime import datetime

list_of_stocks = ['MSFT', 'ING', 'RABO']
print('List of possible stocks: ', list_of_stocks)
stockName = input("Which stock do you want to purchase? ")
volume = input("How many stocks do you want to purchase? ")
dateOfPurchase = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
orderId = 1

stock = Stock(stockName)
stockPrice = stock.retrieve_stock_price_hist(dateOfPurchase)

order1 = Order(stockName, volume, dateOfPurchase, orderId)

stock.retrieve_stock_price_hist()


