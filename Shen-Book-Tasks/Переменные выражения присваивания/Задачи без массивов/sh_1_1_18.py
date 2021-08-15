def sh_1_1_18(a: int, b: int) -> int :
    """
        Вычисление НОД по агоритму Евклида с числом действий log k
    """

    d = 1

    while not(a == 0 or b == 0):
        if a % 2 == 0 and b % 2 == 0:
            d /= 2
            a //= 2
            b //= 2
        elif a % 2 == 0 and b % 2 == 1:
            a //= 2
        elif a % 2 == 1 and b % 2 == 0:
            b //= 2
        elif a % 2 == 1 and b % 2 == 1 and a >= b:
            a -= b
        elif a % 2 == 1 and b % 2 == 1 and a < b:
            b -= a

    if a == 0:
        return d * b

    return d * a


if __name__ == '__main__':

    import random

    num_tests = random.randrange(1, 1000, 1)
    random_values = []

    for __ in range(num_tests):
        random_values.append((random.randrange(1, 10000, 1), random.randrange(1, 10000, 1)))

    print('Check', num_tests, 'examples...')

    for i in random_values:
        assert i[0] % sh_1_1_18(i[0], i[1]) == 0 and i[1] % sh_1_1_18(i[0], i[1]) == 0

    print('Done!')