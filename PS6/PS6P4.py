employeeCount = 0
totalGrossPay = 0
continueLoop = "Yes"
while continueLoop == "Yes":
    lastName = input("Enter employee last name: ")
    hoursWorked = float(input("Enter hours worked: "))
    rateOfPay = float(input("Enter rate of pay: "))
    if hoursWorked > 40:
        regularPay = 40 * rateOfPay
        overtimePay = (hoursWorked - 40) * rateOfPay * 1.5
        grossPay = regularPay + overtimePay
    else:
        grossPay = hoursWorked * rateOfPay
    totalGrossPay += grossPay
    employeeCount += 1
    print("Last name:", lastName)
    print("Gross pay:", grossPay)
    continueLoop = input("Do you want to continue the loop? (Enter Yes to continue): ")
print("Total gross pay:", totalGrossPay)
print("Number of employees:", employeeCount)
print("Average pay:", totalGrossPay/employeeCount)