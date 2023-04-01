def nextMonthsForecast(month, sales):
    forecastPercent = 0
    if month in ["Jan", "Feb", "Mar"]:
        forecastPercent = 0.10
    elif month in ["Apr", "May", "Jun"]:
        forecastPercent = 0.15
    elif month in ["Jul", "Aug", "Sep"]:
        forecastPercent = 0.20
    elif month in ["Oct", "Nov", "Dec"]:
        forecastPercent = 0.25
    else:
        print("Invalid month. Please enter the correct month.")
    nextMonthSales = sales * (1 + forecastPercent)
    return nextMonthSales
def main():
    while True:
        continueProgram = input("Do you want to continue the program? (Yes or No): ")
        if continueProgram.lower() == "yes":
            lastName = input("Enter your last name: ")
            month = input("Enter the month (e.g., Jan, Feb, Mar, etc.): ")
            sales = float(input("Enter the sales: "))

            nextMonthSales = nextMonthsForecast(month, sales)
            print(f"Next month's sales forecast for {lastName}: ${nextMonthSales:.2f}")
        elif continueProgram.lower() == "no":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter Yes or No.")
if __name__ == "__main__":
    main()