class matrix:

    def addition(m1, m2):
        newMatrix = [[0,0], [0,0]]
        for i in range(len(m1)):
            for j in range(len(m2)):
                newMatrix[i][j] = m1[i][j] + m2[i][j]

        return newMatrix

    def subtraction(m1, m2):
        newMatrix = [[0,0], [0,0]]
        for i in range(len(m1)):
            for j in range(len(m2)):
                newMatrix[i][j] = m1[i][j] - m2[i][j]

        return newMatrix


    def multiply(m1, m2):
        newMatrix = [[0,0], [0,0]]
        try:
            for i in range(2):
                for j in range(2):
                    newMatrix[i][j] = m1[i][j] * m2[i][j]
        except TypeError:
            for i in range(2):
                for j in range(2):
                    newMatrix[i][j] = m1[i] * m2[j]

        return newMatrix

b = [[1,2], [3,4]]
c = [[2,3], [4,5]] 

sum1 = matrix.addition(b,c)
sum2 = matrix.multiply(sum1, sum1)
sum3 = matrix.multiply(b,c)
sum4 = matrix.subtraction(sum2, sum3)
print(sum4)
         
