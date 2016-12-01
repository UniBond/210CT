userInput = int(input("> "))

newUserInput = userInput - 1 
num = userInput

while newUserInput > 0:
    if newUserInput > 0:
        num = num * newUserInput
        newUserInput -= 1
        
nFunc = str(num)[::-1]

def factorialFunction(args):
    zeroCount = 0
    for i in range(len(args)):
        if args[i] == '0':
            zeroCount += 1
        else:
            return("Number of trailing zero's: " + str(zeroCount)) 

print(factorialFunction(nFunc))
