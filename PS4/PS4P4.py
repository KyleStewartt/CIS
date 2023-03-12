applianceName = input("Enter the name of the appliance: ")
applianceCost = float(input("Enter the cost of the appliance: "))
if applianceCost > 1000:
    warrantyCost = applianceCost * 0.1
else:
    warrantyCost = applianceCost * 0.05
totalCost = applianceCost + warrantyCost
print("Name of Appliance: " + applianceName)
print("Cost of Appliance: $" + str(applianceCost))
print("Cost of Warranty: $" + str(warrantyCost))
print("Total Cost: $" + str(totalCost))