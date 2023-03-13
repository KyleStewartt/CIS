quantity = float(input("Enter quantity: "))
price = float(input("Enter price: "))

def total(quantity, price):
    total = quantity * price
    if (total > 10000.00):
        return total * 0.9
    else:
        return total

print(f"Quantity: {quantity}")
print(f"Price: {price}")
print(f"Total: {total(quantity,price):.3f}")