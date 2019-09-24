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

UserInput = "Y"

while UserInput.lower() == "y":

    Action_1 = input('What do you wish to do? (choose from: "Add Order", "View Portfolio")')

    if Action_1.lower() == "view portfolio":
        # return portfolio
        print("View Portfolio") # Add optionality
    elif Action_1.lower() == "add order":
        # add order
        NewOrExisting = input("Do you already have a portfolio with us? (Y/N)")
        portfolioName = input("What is the name of the portfolio?")
        stockName = input("Which stock do you want to purchase? Please input ticker ")
        volume = int(input("How many stocks do you want to purchase? "))

        dateOfPurchase = datetime.now().strftime('%Y-%m-%d')
        stock = Stock(stockName)
        stockPriceAtPurchase = stock.retrieve_stock_price_now()

        if NewOrExisting.lower() == "n":
            ownerName = input("What is your name?")
            newPortfolio = Portfolio(portfolioName, ownerName)

        elif NewOrExisting.lower() == "y":
            ownerName = input("What is your name?")
            newPortfolio = Portfolio(portfolioName, ownerName)

        orderId = len(newPortfolio.Orders) + 1
        newOrder = Order(stock, volume, stockPriceAtPurchase, dateOfPurchase, orderId, newPortfolio.Name)

        newPortfolio.AddOrder(newOrder)
        portfolioReturn = newPortfolio.CalculateReturn()

    else:
        print("Incorrect input, please try again")

    UserInput = input('Do you wish to continue? (Y/N)')

print("Thanks for visiting!")
######################################
# Export new order functionality
######################################

