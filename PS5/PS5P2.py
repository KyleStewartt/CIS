def calculateCost():
    partNumber = input("Enter the part number: ")
    quantity = int(input("Enter the quantity: "))
    if partNumber == "10" or partNumber == "55" or int(partNumber) == 10 or int(partNumber) == 55:
        unitCost = 1.00
    elif partNumber == "99" or int(partNumber) == 99:
        unitCost = 2.00
    elif partNumber == "80" or partNumber == "70" or int(partNumber) == 80 or int(partNumber) == 70:
        unitCost = 3.00
    else:
        unitCost = 5.00
    totalCost = quantity * unitCost
    print("Part Number: " + str(partNumber))
    print("Unit Cost: $" + str(unitCost))
    print("Total Cost: $" + str(totalCost))
# Example usage:
calculateCost()