def binarySearch(theList, num):
    firstNumber = 0 #Start from 0
    lastNumber = len(theList) - 1
    numberFound = False

    while firstNumber <= lastNumber and not numberFound:
        middleValue = (firstNumber + lastNumber) // 2
        if theList[middleValue] == num:
            numberFound = True

        else:
            if num < theList[middleValue]:
                lastNumber = middleValue - 1
            else:
                firstNumber = middleValue + 1
    return numberFound


print(binarySearch([1,3,5,6,7,3,8,22,19,1], 22))
