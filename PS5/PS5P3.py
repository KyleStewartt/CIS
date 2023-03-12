def calculateInterest():
    principle = float(input("Enter the principle amount: "))
    yearsToMaturity = int(input("Enter the years to maturity: "))
    if principle > 100000 and yearsToMaturity == 5:
        interestRate = 0.06
    elif 50000 <= principle <= 100000 and yearsToMaturity == 10:
        interestRate = 0.05
    elif 50000 <= principle <= 100000 and yearsToMaturity == 5:
        interestRate = 0.04
    else:
        interestRate = 0.02
    interestAmount = principle * interestRate
    print("Principle: $" + str(principle))
    print("Interest Rate: " + str(interestRate*100) + "%")
    print("Interest Amount (1st year): $" + str(interestAmount))
# Example usage:
calculateInterest()