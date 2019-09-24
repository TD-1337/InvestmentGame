from datetime import datetime


OrderID = 1

input_list_stocks = ["ING", "ABN Amro", "Rabobank"]

Stock = input("Which stock do you want to purchase? ", input_list_stocks)
Volume = input("How many stocks do you want to purchase? ")
DateOfPurchase = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


print('You bought', Volume, 'number of', Stock, 'stocks, at', DateOfPurchase, '. OrderID=', OrderID, sep = '')

#return Stock + Volume + Date + Order ID

OrderID += 1


