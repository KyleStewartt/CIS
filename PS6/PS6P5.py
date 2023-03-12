discountTotal = 0
continueLoop = "Yes"
while continueLoop == "Yes":
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price of item: "))
    extendedPrice = quantity * price
    if extendedPrice > 10000:
        discountPercent = 0.25
    else:
        discountPercent = 0.1
    discountAmount = extendedPrice * discountPercent
    total = extendedPrice - discountAmount
    print("Extended price:", extendedPrice)
    print("Discount amount:", discountAmount)
    print("Total:", total)
    discountTotal += discountAmount
    continueLoop = input("Do you want to continue the loop? (Enter Yes to continue): ")
print("Sum of all discounts:", discountTotal)