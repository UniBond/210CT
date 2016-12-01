#imports random module, allows use of random functions within this program
import random
#variable declaration. the array of numbers to be shuffled
inputArray = [5,3,8,6,1,9,2,7]

#function definition. takes 1 argument (the above array)
def arrayShuffle(inputArray):
    #variable declaration.  empty to start.
    outputArray = []
    #print the original array. Allows you to see before and after
    print("Original Array: " + str(inputArray))
    #for loop. Iterates over the length of the array
    for i in range(len(inputArray)):
        #r variable. chooses random int between 0 and length of the array.
        r = random.randint(0, len(inputArray))
        #r - 1, array begins from 0 in python.
        r = r-1
        #append inputArray[r] to outputArray, remove inputArray[r] from inputArray, continue loop
        outputArray.append(inputArray[r])
        inputArray.remove(inputArray[r])
    #loop completed. return outputArray
    return("New Array: " + str(outputArray))

#print above function. tests if it works
print(arrayShuffle(inputArray))

