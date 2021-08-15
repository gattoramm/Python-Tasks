def sh_1_1_14(a: int, b: int) -> int:
    """
        Вычисление НОД(a,b) модифицированным вариантом алгоритма Евклида.
    """

    if a < b:
        a, b = b, a

    while not(0 == b or 0 == a % b):
        a = a % b
        if a < b:
            a, b = b, a

    return b


if __name__ == '__main__':

    import random

    num_tests = random.randrange(1, 1000, 1)
    random_values = []

    for __ in range(num_tests):
        random_values.append((random.randrange(1, 10000, 1), random.randrange(1, 10000, 1)))

    print('Check', num_tests, 'examples...')

    for i in random_values:
        assert i[0] % sh_1_1_14(i[0], i[1]) == 0 and i[1] % sh_1_1_14(i[0], i[1]) == 0

    print('Done!')
