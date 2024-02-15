"""Написать функцию, которая вернет матрицу 3х3, заполненную уникальными случайными числами от 1 до N.
Signature функции: func getMatrix() [][]int {}
Пример матрицы если N=20:
    [ [ 4,  7,  13 ],
      [ 14, 3,  6  ],
      [ 1,  18, 10 ] ]
"""


import random


def get_matrix(dim: int, n: int) -> list:

    d = list()
    while len(d) < (dim ** 2):
        value = random.randint(1, n)
        if value not in d:
            d.append(value)

    matrix = []

    while d:
        matrix.append(d[:dim])
        d = d[dim:]

    return matrix


if __name__ == '__main__':
    print(get_matrix(3, 20))
