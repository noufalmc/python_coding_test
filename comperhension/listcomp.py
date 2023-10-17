list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_new = [x ** 2 for x in list]

even_list = [i for i in list if i % 2 == 0]
odd_list = [i for i in list if i % 2 != 0]

# Find all of the numbers from 1–100 that are divisible by 8

num8 = [x for x in range(1, 97) if x % 8 == 0]

# Find all of the numbers from 1–1000 that have a 6 in them
num6 = [x for x in range(1, 100) if '6' in str(x)]

# Count the number of spaces in a string
string = "Practice Problems to Drill List Comprehension in Your Head."
spaces = [x for x in string if x == ' ']
vowels = [x for x in string if x not in ['a', 'e', 'i', 'o', 'u']]

print(list)
print(list_new)
print(even_list)
print(odd_list)
print("Divisible 8")
print(num8)
print(num6)
print("Total Space is " + str(len(spaces)))
print("After vowel removal is")
print(''.join(vowels))
