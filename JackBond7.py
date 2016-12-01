newInt = int(input("> "))

def primeNumber(num, n):
    newNum = num % n
    if n <= 1:
        print(str(num) + " is a prime number!")
        return
    if newNum == 0:
        print(str(num) + " is not a prime number!")
        return
    primeNumber(num, n-1)

primeNumber(newInt, newInt-1)
