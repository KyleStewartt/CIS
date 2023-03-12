itemQuantity = int(input("Enter quantity of item: "))
if itemQuantity >= 1000:
    unitPrice = 3.00
else:
    unitPrice = 5.00
extendedPrice = itemQuantity * unitPrice
tax = extendedPrice * 0.07
total = extendedPrice + tax
print("Quantity:", itemQuantity)
print("Unit Price:", unitPrice)
print("Extended Price:", extendedPrice)
print("Tax:", tax)
print("Total:", total)