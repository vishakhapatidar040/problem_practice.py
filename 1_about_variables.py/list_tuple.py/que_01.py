#multiple pallindrome
list1 = [121, 123, 1221, 12321, 123321]
for i in list1:
    if str(i) == str(i)[::-1]:
        print(i, "is a pallindrome")
    else:
        print(i, "is not a pallindrome")