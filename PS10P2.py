def computeSquareFootage(length, width, height):
    floorAndCeiling = 2 * length * width
    twoWallsLengthHeight = 2 * length * height
    twoWallsWidthHeight = 2 * width * height
    squareFootage = floorAndCeiling + twoWallsLengthHeight + twoWallsWidthHeight
    return squareFootage
def gallonsOfPaint(squareFootage):
    gallonsNeeded = squareFootage / 50
    return gallonsNeeded
def main():
    while True:
        continueProgram = input("Do you want to continue the program? (Yes or No): ")
        if continueProgram.lower() == "yes":
            length = float(input("Enter the length of the room: "))
            width = float(input("Enter the width of the room: "))
            height = float(input("Enter the height of the room: "))

            squareFootage = computeSquareFootage(length, width, height)
            gallonsNeeded = gallonsOfPaint(squareFootage)
            print(f"Gallons of paint needed to paint the room: {gallonsNeeded:.2f}")
        elif continueProgram.lower() == "no":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter Yes or No.")
if __name__ == "__main__":
    main()