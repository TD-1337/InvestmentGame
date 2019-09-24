class Order:

    def __init__(self,Stock, Volume, DateOfPurchase, OrderID):
        self.Stock = Stock
        self.Volume = Volume
        self.DateOfPurchase = DateOfPurchase
        self.OrderID = OrderID


########## Dit moet in de main denk ik
from datetime import datetime

list_of_stocks = ['ABN', 'ING', 'RABO']
print('List of possible stocks: ',list_of_stocks)

Stock = input("Which stock do you want to purchase? ")
Volume = input("How many stocks do you want to purchase? ")
DateOfPurchase = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
OrderID += 1


## hier roep je de class Order aan met oplopende Order ID
S1 = Order(Stock,Volume,DateOfPurchase,OrderID)

print('You bought ', S1.Volume, ' number of ', S1.Stock, ' stocks, at ', S1.DateOfPurchase, '. OrderID= ', S1.OrderID, sep = '')

#return Stock + Volume + Date + Order ID



