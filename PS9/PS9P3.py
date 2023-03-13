destination = input("Enter destination city: ")
miles = float(input("Enter miles travelled: "))
gallons = float(input("Enter gallons used: "))

def mpg(miles, gallons):
    return miles/gallons

def cost(gallons):
    return gallons*2.50

print(f"Destination City: {destination}")
print(f"Miles per Gallons: {mpg(miles,gallons):.3f}")
print(f"Cost of Gas: {cost(gallons):.3f}")
