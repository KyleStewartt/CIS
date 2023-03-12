make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
msrp = float(input("Enter the MSRP of the car: "))
discountPercent = float(input("Enter the discount percent as a decimal: "))
amountOff = msrp * discountPercent
discountedPrice = msrp - amountOff
print("Make: ", make)
print("Model: ", model)
print("MSRP: $", msrp)
print("Discount Percent: ", discountPercent * 100, "%")
print("Amount Off MSRP: $", amountOff)
print("Discounted Price: $", discountedPrice)