def even_squares(x):
  for i in range(x):
      if i**2%2==0:
          yield i**2


print(list(even_squares(14)))
