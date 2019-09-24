from Order import Order
from Stock import Stock
from Portfolio import Portfolio
from datetime import datetime

######################################
# Import existing order functionality
######################################

### import class which imports content of csv to Portfolio / Order objects

######################################
# Add new order
######################################

# Ask user what he/she wants to do

### Add order or multiple orders
### View portfolio / returns
### Sell (optional)


portfolioName = "My Portfolio"
ownerName = "Stef"

newPortfolio = Portfolio(portfolioName, ownerName)

stockName = input("Which stock do you want to purchase? Please input ticker ")
volume = int(input("How many stocks do you want to purchase? "))

dateOfPurchase = datetime.now().strftime('%Y-%m-%d')

stock = Stock(stockName)
stockPriceAtPurchase = stock.retrieve_stock_price_now()

orderId = len(newPortfolio.Orders) + 1
newOrder = Order(stock, volume, stockPriceAtPurchase, dateOfPurchase, orderId, newPortfolio.Name)

newPortfolio.AddOrder(newOrder)
portfolioReturn = newPortfolio.CalculateReturn()

######################################
# Export new order functionality
######################################

