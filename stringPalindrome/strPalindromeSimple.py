def check_palindrome(str):
    str_rev = str[::-1]
    if str == str_rev:
        print(str + " Palindrome")
    else:
        print("Not Palindrome")


def check_pal(str):
    length = len(str)
    flag = True
    for e in range(1):
        if str[0] != str[length-e-1]:
            flag = False
            break
    return flag


string = input("Enter a string  ")
check_palindrome(string)
string = input("Enter second string  ")
print(check_pal(string))
