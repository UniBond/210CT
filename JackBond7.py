#Gets user input
newInt = int(input("> "))

#function that works out if a number is a prime number
def primeNumber(num, n):
    newNum = num % n #variable. num argument, moduler n argument, newNum = remainder
    #print(str(newNum) + ", " + str(num) + ", " + str(n)) testing
    if n <= 1: #if n < 1, then its prime!
        print(str(num) + " is a prime number!")
        return
    if newNum == 0: #if remainder is 0, its been divided perfectly, no remainder
        print(str(num) + " is not a prime number!")
        return
    #recursive call, keeps reducing to see if prime
    primeNumber(num, n-1) 


#function call. allows for testing, with arguments from users input
primeNumber(newInt, newInt-1)
        


#PRIMENUMBER(NUM, N)
#   INT = NUM modulo n
#   if n <<- 1
#       RETURN TRUE
#   if INT <-<- 0
#       RETURN FALSE
#   primeNumber(num, n-1)
