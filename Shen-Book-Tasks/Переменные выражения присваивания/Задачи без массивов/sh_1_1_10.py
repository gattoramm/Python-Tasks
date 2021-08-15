def sh_1_1_10(n: int) -> int:
    """
        Вычисление последовательности Фибоначчи через умножение матрицы
    """

    def multiply_matrix(M, T):

        r = [[0, 0], [0, 0]]
        r[0][0] = T[0][0] * M[0][0] + T[0][1] * M[1][0]
        r[0][1] = T[0][0] * M[0][1] + T[0][1] * M[1][1]
        r[1][0] = T[1][0] * M[0][0] + T[1][1] * M[1][0]
        r[1][1] = T[1][0] * M[0][1] + T[1][1] * M[1][1]

        return r

    M = [[1, 1], [1, 0]]
    T = [[1, 0], [0, 1]]

    while n > 0:
        if n % 2 == 0:
            n /= 2
            M = multiply_matrix(M, M)
        n -= 1
        T = multiply_matrix(T, M)

    return T[0][1]


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_10(1) == 1
    assert sh_1_1_10(0) == 0
    assert sh_1_1_10(4) == 3
    assert sh_1_1_10(15) == 610
    assert sh_1_1_10(10) == 55

    print('Done!')
