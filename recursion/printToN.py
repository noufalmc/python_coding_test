def printToN(n):
    if n > 0:
        printToN(n-1)
        print(n, end=' ')

limit = int(input("Enter Limit  "))
printToN(limit)