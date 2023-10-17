def min_max(li):
    min1, max1 = li[0]
    for i in li:
        if i > max1:
            max1 = i
        if min1 > i:
            min1 = i
    print("Max is " + str(max1))
    print("Min is " + str(min1))


li = []
n = int(input("Enter the size of the list ?? "))
for i in range(n):
    ele = input()
    li.append(ele)
min_max(li)
