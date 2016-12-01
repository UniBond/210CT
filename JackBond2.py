#allows user to input number.
userInput = int(input("> "))

#variable declaration. variables hold some information
newUserInput = userInput - 1 
num = userInput

#while loop, runs while user input is greater than 1
while newUserInput > 0:
    #if statement is useless, can be removed?
    if newUserInput > 0:
        num = num * newUserInput
        newUserInput -= 1

#variable declaration.  flip number backwards
nFunc = str(num)[::-1]

#function definition. takes 1 argument
def factorialFunction(args):
    #variable declaration, counts number of zeros
    zeroCount = 0
    #loop over length of argument (each number).
    for i in range(len(args)):
        #if number is equal to zero, increase zeroCount variable by 1
        if args[i] == '0':
            zeroCount += 1
        #runs if number isnt equal to zero. return and exit program
        else:
            return("Number of trailing zero's: " + str(zeroCount)) 


#testing purposes, allows program to run
print(factorialFunction(nFunc))
