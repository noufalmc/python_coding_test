def print_pattern(n):
    diff = n
    start = 1
    
    for i in range(n):
        print("#", end=" ")
        val = start
        for j in range(i + 1):
            print(val - j, end=' ')
            val-= (n-i-j)
        print()
        start += diff
        diff -= 1



n=int(input("Enter number of length need to be print:: "))
print()
for _ in range(n+10):
    print("***", end="")
print()
print()
print_pattern(n)
print()
for _ in range(n+10):
    print("***", end="")
