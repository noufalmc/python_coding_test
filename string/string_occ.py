def str_occr(str):
    occ = {}
    for i in str.lower():
        if i in occ:
            occ[i] = occ[i]+1
        else:
            occ[i] = 1
    print(occ)


str = input("Enter string ")
str_occr(str)
