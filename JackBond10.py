def sequence(listVar):
    finalList = []
    tempList = []
    num = 0
    
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
    

listVar = [1,2,3,4,1,5,1,6,7]
print(sequence(listVar))
