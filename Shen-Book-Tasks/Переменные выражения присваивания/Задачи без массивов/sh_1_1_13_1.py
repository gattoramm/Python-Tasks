def sh_1_1_13_1(a: int, b: int) -> int:
    """
        Вычисление НОД(a,b).
    """

    nod = max(a, b)

    while not(a % nod == 0 and b % nod == 0):
        nod -= 1

    return nod


if __name__ == '__main__':

    import random

    num_tests = random.randrange(1, 1000, 1)
    random_values = []

    for __ in range(num_tests):
        random_values.append((random.randrange(1, 10000, 1), random.randrange(1, 10000, 1)))

    print('Check', num_tests, 'examples...')

    for i in random_values:
        assert i[0] % sh_1_1_13_1(i[0], i[1]) == 0 and i[1] % sh_1_1_13_1(i[0], i[1]) == 0

    print('Done!')