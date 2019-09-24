from Order import Order
from Stock import Stock
from Portfolio import Portfolio
from datetime import datetime

portfolioName = "My Portfolio"
ownerName = "Stef"

newPortfolio = Portfolio(portfolioName, ownerName)

list_of_stocks = ['MSFT', 'ING', 'RABO']
print('List of possible stocks: ', list_of_stocks)
#stockName = input("Which stock do you want to purchase? ")
stockName = 'MSFT'
volume = 10
#volume = input("How many stocks do you want to purchase? ")
dateOfPurchase = datetime.now().strftime('%Y-%m-%d')
orderId = 1

stock = Stock(stockName)
stockPriceAtPurchase = stock.retrieve_stock_price_EOD(dateOfPurchase)
newOrder = Order(stockName, volume, stockPriceAtPurchase, dateOfPurchase, orderId)

newPortfolio.AddOrder(newOrder)
valueAtPurchase = newPortfolio.ValueAtPurchaseDate()
valueNow = newPortfolio.CalculateValue()


