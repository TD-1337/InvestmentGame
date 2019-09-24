from Order import Order
from Stock import Stock
import Portfolio

#list_of_stocks = ['ABN', 'ING', 'RABO']
#print('List of possible stocks: ', list_of_stocks)
#stock = input("Which stock do you want to purchase? ")
#volume = input("How many stocks do you want to purchase? ")
#dateOfPurchase = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#orderId = 1

#order1 = Order(stock, volume, dateOfPurchase, orderId)

stock = Stock("MSFT")
print(stock.retrieve_stock_price_now())
print(stock.retrieve_stock_price_EOD("2019-09-23"))



