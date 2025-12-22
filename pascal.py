# Simple Pascal's triangle test code to practice GitHub basics. 

def factorial(n):
    num = 1
    for i in range(n):
        num *= (i+1)
    return num

def choose(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

def binomial(N):
    for i in range(N+1):
        numlist = []
        for j in range(i+1):
            numlist.append(choose(i,j))
        print(numlist)

binomial(5)