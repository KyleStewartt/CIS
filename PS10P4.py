def computeTicketPrice(milesFromDowntown):
    if milesFromDowntown >= 30:
        ticketPrice = 12
    elif 20 <= milesFromDowntown <= 29:
        ticketPrice = 10
    elif 10 <= milesFromDowntown <= 19:
        ticketPrice = 8
    else:
        ticketPrice = 5
    return ticketPrice
def main():
    totalTicketPrice = 0
    while True:
        continueProgram = input("Do you want to continue the program? (Yes or No): ")
        if continueProgram.lower() == "yes":
            lastName = input("Enter your last name: ")
            milesFromDowntown = int(input("Enter the miles from downtown Chicago: "))
            ticketPrice = computeTicketPrice(milesFromDowntown)
            print(f"Train ticket price for {lastName}: ${ticketPrice:.2f}")
            totalTicketPrice += ticketPrice
        elif continueProgram.lower() == "no":
            print("Exiting the program.")
            print(f"Total price of all tickets: ${totalTicketPrice:.2f}")
            break
        else:
            print("Invalid input. Please enter Yes or No.")
if __name__ == "__main__":
    main()