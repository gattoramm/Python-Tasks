def sh_1_1_13_2(a: int, b: int) -> int:
    """
        Вычисление НОД(a,b) алгоритмом Евклида.
    """

    m, n = a, b

    while not(m == 0 or n == 0):
        if n > m:
            n -= m
        else:
            m -= n

    if m == 0: return n

    return m


if __name__ == '__main__':

    import random

    num_tests = random.randrange(1, 1000, 1)
    random_values = []

    for __ in range(num_tests):
        random_values.append((random.randrange(1, 10000, 1), random.randrange(1, 10000, 1)))

    print('Check', num_tests, 'examples...')

    for i in random_values:
        assert i[0] % sh_1_1_13_2(i[0], i[1]) == 0 and i[1] % sh_1_1_13_2(i[0], i[1]) == 0

    print('Done!')
