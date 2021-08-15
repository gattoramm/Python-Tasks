def sh_1_1_17(a: int, b: int) -> (int, int):
    """
        Вычисление НОД и НОК алгоритмом Дейкстры
    """

    m = v = a
    n = u = b

    while not(m == 0 or n == 0):
        if m >= n:
            m -= n
            v += u
        else:
            n -= m
            u += v

    if m == 0:
        return n, v

    return m, u

if __name__ == '__main__':

    import random

    num_tests = random.randrange(1, 1000, 1)
    random_values = []

    for __ in range(num_tests):
        random_values.append((random.randrange(1, 10000, 1), random.randrange(1, 10000, 1)))

    print('Check', num_tests, 'examples...')

    for i in random_values:
        assert (2* i[0] * i[1]) / sh_1_1_17(i[0], i[1])[0] == sh_1_1_17(i[0], i[1])[1]

    print('Done!')


