def mygen(x):
    i = 0
    while i < x:
        if i % 2 == 0:
            yield 'Even'
        else:
            yield 'Odd'
        i += 1


for i in mygen(10):
    print(i)
