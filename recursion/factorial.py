def recursion_factorial(x):
    if x == 1:
        return 1
    else:
        return x * recursion_factorial(x - 1)


fact = int(input("Enter a number to be factorial wants?"))
result = recursion_factorial(fact)
print("Factorail of "+str(fact)+" = "+str(result))