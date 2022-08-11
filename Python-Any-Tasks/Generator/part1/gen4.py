mylist = [1, 3, 5, 7]
s1 = [x**2 for x in mylist]
s2 = (x**2 for x in mylist)
print(s1)
print(s2)