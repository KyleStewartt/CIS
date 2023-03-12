studentCount = 0
continueLoop = "Yes"
while continueLoop == "Yes":
    lastName = input("Enter last name: ")
    exam1 = float(input("Enter exam 1 score: "))
    exam2 = float(input("Enter exam 2 score: "))
    averageScore = (exam1 + exam2) / 2
    print("Last name:", lastName)
    print("Average exam score:", averageScore)
    studentCount += 1
    continueLoop = input("Do you want to continue the loop? (Enter Yes to continue): ")
print("Number of students entered:", studentCount)