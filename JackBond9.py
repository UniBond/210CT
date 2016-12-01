def binarySearch(theList, num1, num2):
    firstNumber = 0
    lastNumber = len(theList) - 1
    numberFound = False

    while firstNumber <= lastNumber and not numberFound:
        middleValue = (firstNumber + lastNumber) // 2
        if theList[middleValue] > num1 and theList[middleValue] < num2:
            numberFound = True

        else:
            if num1 < theList[middleValue]:
                lastNumber = middleValue - 1
            else:
                firstNumber = middleValue + 1
    return numberFound


print(binarySearch([2,3,5,7,9,13], 10, 13))
