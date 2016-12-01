import math

def highestSquare(num):
    if num >= 1:
        numInt = math.sqrt(num)
        numInt = int(numInt)
        return("Closest square root for the number entered is: " + str(numInt)
               + "\nWhich is the square root of: " + str(numInt*numInt))
    else:
        return("That number is zero or below. Please choose a positive integer")

print(highestSquare(3200000))
