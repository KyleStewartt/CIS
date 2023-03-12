lastName = input("Enter the user's last name: ")
numDependents = int(input("Enter the number of dependents: "))
grossIncome = float(input("Enter the gross income: "))
adjGrossIncome = grossIncome - numDependents * 12000
taxRate = 0.2 if adjGrossIncome > 50000 else 0.1
incomeTax = adjGrossIncome * taxRate
if incomeTax < 0:
    incomeTax = 100
print(f"Last Name: {lastName}")
print(f"Gross Income: ${grossIncome:.2f}")
print(f"Number of Dependents: {numDependents}")
print(f"Adjusted Gross Income: ${adjGrossIncome:.2f}")
print(f"Income Tax: ${incomeTax:.2f}")