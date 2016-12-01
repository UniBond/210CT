import random
inputArray = [5,3,8,6,1,9,2,7]


def arrayShuffle(inputArray):
    outputArray = []
    print("Original Array: " + str(inputArray))
    for i in range(len(inputArray)):
        r = random.randint(0, len(inputArray))
        r = r-1
        outputArray.append(inputArray[r])
        inputArray.remove(inputArray[r])
    return("New Array: " + str(outputArray))


print(arrayShuffle(inputArray))

