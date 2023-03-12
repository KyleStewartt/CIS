def calculateCost():
    numTickets = int(input("Enter the number of concert tickets: "))
    if numTickets >= 25:
        pricePerTicket = 50
    elif numTickets >= 10:
        pricePerTicket = 60
    elif numTickets >= 5:
        pricePerTicket = 70
    else:
        pricePerTicket = 75
    totalCost = numTickets * pricePerTicket
    print("Number of tickets: " + str(numTickets))
    print("Price per ticket: $" + str(pricePerTicket))
    print("Total cost: $" + str(totalCost))
# Example usage:
calculateCost()