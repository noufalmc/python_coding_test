def string_palindrome(string):
    n = len(string)
    print(n//2)
    x = 0
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            x = 1
            break
    if x == 0:
        print(string + " is palindrome")
    else:
        print(i)
        print(string + " is not palindrome")


str_name = input("Enter String  ")

string_palindrome(str_name)
