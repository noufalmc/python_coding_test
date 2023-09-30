def check_palindrome(str):
    str_rev = str[::-1]
    if str == str_rev:
        print(str + " Palindrome")
    else:
        print("Not Palindrome")


string = input("Enter a string  ")
check_palindrome(string)
