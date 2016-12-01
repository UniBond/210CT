#Imports the math module for use within this program
import math

#defines a function with 1 argument
def highestSquare(num):
    #function runs only if argument is greater than or equal to 1 (positive integer)
    if num >= 1:
        #variable declaration
        numInt = math.sqrt(num) #square root the number
        numInt = int(numInt) #convert number to integer (always rounds down), which is closest square number
        return("Closest square root for the number entered is: " + str(numInt)
               + "\nWhich is the square root of: " + str(numInt*numInt))
    #runs if num is less than 1
    else:
        return("That number is zero or below. Please choose a positive integer")

#prints, for testing purposes
print(highestSquare(3200000))
