def counter(n):
    i = 0
    while i <= n:
        yield i
        i += 1


for i in counter(4):
    print(i)
