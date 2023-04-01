def outTheDoorPrice(msrp, make, model, evCode):
    percentOffMsrp = 0
    if make.lower() == "honda" and model.lower() == "accord":
        percentOffMsrp = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        percentOffMsrp = 0.15
    elif evCode.lower() == "y":
        percentOffMsrp = 0.30
    else:
        percentOffMsrp = 0.05
    newMsrp = msrp * (1 - percentOffMsrp)
    salesTax = newMsrp * 0.07
    totalPrice = newMsrp + salesTax
    return totalPrice, newMsrp
def main():
    totalMsrp = 0
    totalSalesPrice = 0
    while True:
        continueProgram = input("Do you want to continue the program? (Yes or No): ")
        if continueProgram.lower() == "yes":
            make = input("Enter the make of the automobile: ")
            model = input("Enter the model of the automobile: ")
            evCode = input("Is the automobile an electric vehicle? (Y or N): ")
            msrp = float(input("Enter the MSRP (sticker price) of the automobile: "))
            totalPrice, newMsrp = outTheDoorPrice(msrp, make, model, evCode)
            print(f"Out the door price for {make} {model}: ${totalPrice:.2f}")
            totalMsrp += msrp
            totalSalesPrice += totalPrice
        elif continueProgram.lower() == "no":
            print("Exiting the program.")
            print(f"Total MSRP of all automobiles: ${totalMsrp:.2f}")
            print(f"Total sales price of all automobiles: ${totalSalesPrice:.2f}")
            break
        else:
            print("Invalid input. Please enter Yes or No.")
if __name__ == "__main__":
    main()