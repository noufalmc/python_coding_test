def fib(n):
    a = 0
    b = 1
    c = 0
    count = 1
    if n < 0:
        print("Invalid number")
    elif n == 0:
        print("Invalid")
    else:
        while count <= n:
            print(c)
            c = a + b
            a = b
            b = c
            count += 1


n = int(input("Enter number of series to be want??  "))
fib(n)
