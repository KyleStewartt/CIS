def computeAssessedValue(county, marketValue):
    if county.lower() == "cook":
        assessedValuePercent = 0.90
    elif county.lower() == "dupage":
        assessedValuePercent = 0.80
    elif county.lower() == "mchenry":
        assessedValuePercent = 0.75
    elif county.lower() == "kane":
        assessedValuePercent = 0.60
    else:
        assessedValuePercent = 0.70

    assessedValue = marketValue * assessedValuePercent
    return assessedValue
def main():
    totalMarketValue = 0
    totalAssessedValue = 0
    while True:
        continueProgram = input("Do you want to continue the program? (Yes or No): ")
        if continueProgram.lower() == "yes":
            county = input("Enter the county: ")
            marketValue = float(input("Enter the market value of the home: "))

            assessedValue = computeAssessedValue(county, marketValue)
            print(f"Assessed value for the home in {county} County: ${assessedValue:.2f}")

            totalMarketValue += marketValue
            totalAssessedValue += assessedValue
        elif continueProgram.lower() == "no":
            print("Exiting the program.")
            print(f"Total market value of all homes: ${totalMarketValue:.2f}")
            print(f"Total assessed value of all homes: ${totalAssessedValue:.2f}")
            break
        else:
            print("Invalid input. Please enter Yes or No.")
if __name__ == "__main__":
    main()