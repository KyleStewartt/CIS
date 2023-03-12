def calculatePrice():
    quantityOfWidgets = int(input("Enter the quantity of widgets: "))
    if quantityOfWidgets > 10000:
        price = 10
    elif quantityOfWidgets >= 5000 and quantityOfWidgets <= 10000:
        price = 20
    else:
        price = 30
    extendedPrice = quantityOfWidgets * price
    taxAmount = extendedPrice * 0.07
    total = extendedPrice + taxAmount
    print("Extended Price: $" + str(extendedPrice))
    print("Tax Amount: $" + str(taxAmount))
    print("Total: $" + str(total))
# Example usage:
calculatePrice()