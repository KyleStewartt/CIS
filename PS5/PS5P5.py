def calculateBonus():
    lastName = input("Enter employee last name: ")
    salary = float(input("Enter employee salary: "))
    jobLevel = int(input("Enter employee job level: "))
    if jobLevel >= 10:
        bonusRate = 0.25
    elif jobLevel >= 5:
        bonusRate = 0.2
    else:
        bonusRate = 0.1
    bonus = salary * bonusRate
    print("Employee last name: " + lastName)
    print("Bonus: $" + str(bonus))
# Example usage:
calculateBonus()