#Binary search function
def binarySearch(theList, num1, num2):
    #variable declaration
    firstNumber = 0
    lastNumber = len(theList) - 1
    numberFound = False

    #while loop, if firstnumber <= lastNumber and number hasnt been found
    while firstNumber <= lastNumber and not numberFound:
        middleValue = (firstNumber + lastNumber) // 2 #Middle value of list
        if theList[middleValue] > num1 and theList[middleValue] < num2: #True if a value is found
            #that is greater than variable num1, and less than variable num 2
            numberFound = True

        else: #If the above if statement is not true
            if num1 < theList[middleValue]: #If number is less than current
                lastNumber = middleValue - 1 #lastNumber takes middleValue - 1
            else: #If the above ststement is not true
                firstNumber = middleValue + 1 #firstNumber takes middleValue + 1
    return numberFound #if the above while conditions are not met, return


#Allows program to run. contains list, and 2 number arguments
print(binarySearch([2,3,5,7,9,13], 10, 13))
