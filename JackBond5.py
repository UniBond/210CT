class matrix:

    def addition(m1, m2):  #function for adding matrices
        newMatrix = [[0,0], [0,0]]  #define 2 lists within list
        for i in range(len(m1)): #loop length of argument m1
            for j in range(len(m2)): #loop length of argument m2
                newMatrix[i][j] = m1[i][j] + m2[i][j] #append added 
                                                       #matricies to list                                                                                         

        return newMatrix #return

    def subtraction(m1, m2): #function for subtracting matrices
        newMatrix = [[0,0], [0,0]] #define 2 lists within list
        for i in range(len(m1)): #loop length of argument m1
            for j in range(len(m2)): #loop length of argument m2
                newMatrix[i][j] = m1[i][j] - m2[i][j] #append added
                                                       #matricies to list

        return newMatrix #return


    def multiply(m1, m2): #function for multiplying matrices
        newMatrix = [[0,0], [0,0]] #define 2 lists within list
        try:                       #try (allows for exceptions)
            for i in range(2): #loop twice
                for j in range(2): #loop twice
                    newMatrix[i][j] = m1[i][j] * m2[i][j]
        except TypeError: #except TypeError
            for i in range(2): #loop twice
                for j in range(2): #loop twice
                    newMatrix[i][j] = m1[i] * m2[j]

        return newMatrix #return

b = [[1,2], [3,4]]
c = [[2,3], [4,5]] 

sum1 = matrix.addition(b,c)
sum2 = matrix.multiply(sum1, sum1)
sum3 = matrix.multiply(b,c)
sum4 = matrix.subtraction(sum2, sum3)
print(sum4)
         
