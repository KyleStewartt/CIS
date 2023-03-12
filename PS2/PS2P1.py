stockTickerSymbol = input("Enter Stock ticker symbol ")
numberOfShares = float(input("Enter number of shares "))
costPerShare = float(input("Enter cost per share "))
amountInvested = costPerShare * numberOfShares
print("Amount invested in ", stockTickerSymbol, "is ", amountInvested)