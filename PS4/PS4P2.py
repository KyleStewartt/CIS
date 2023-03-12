def calculateExtendedPrice():
    item = input("Enter the item (A or B): ")
    quantity = int(input("Enter the quantity: "))
    if item == "A":
        unit_price = 10.00
    else:
        unit_price = 20.00
    extended_price = quantity * unit_price
    print("Item: " + item)
    print("Unit Price: $" + str(unit_price))
    print("Extended Price: $" + str(extended_price))
calculateExtendedPrice()