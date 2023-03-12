numOfBooks = int(input("Enter the numberOfBooks to order: "))
costPerBook = float(input("Enter the costPerBook: "))
orderTotal = numOfBooks * costPerBook
if orderTotal > 50.00:
    shippingCharge = 0
else:
    shippingCharge = 25.00
print("Order Total: $" + str(orderTotal))
print("Shipping Charge: $" + str(shippingCharge))