#function for sub-sequence extraction
def sequence(listVar):
    #variable declaration
    finalList = []
    tempList = []
    num = 0
    
    #This for loop is to loop over all elements of the function argument
    #It compares each element to it's previous, which allows it to work
    #out when the end of that sub-sequence is
    for i in range(len(listVar)-1): 
        if i == 0: 
            tempList.append(listVar[i])
        else: 
            if listVar[i] >= listVar[i-1]: 
                tempList.append(listVar[i]) 
            if listVar[i] < listVar[i-1]: 
                finalList.append(tempList) 
                tempList = [] 
                tempList.append(listVar[i]) 
    finalList.append(tempList) 

    
	
    #This for loop is to work out which sub-sequence is of greatest length
    #This loop works very similiarly to the one previously
    for i in range(len(finalList)):
        if i == 0:
            num = len(finalList[i])
            listVar = finalList[i]
        else:
            if len(finalList[i]) > num:
                num = len(finalList[i])
                listVar = finalList[i]
    return("The list with the largest length is " + str(listVar) +
           " which contains " + str(num) + " numbers.")
    

#Below allows program to work. Test list, alongside function run and print
listVar = [1,2,3,4,1,5,1,6,7]
print(sequence(listVar))
