def sh_1_1_16(a: int, b: int) -> (int, int, int):
    """
        Вычисление d=НОД(a,b) и целых x и y,что d=a·x+b·y,
        используя алгоритм Евклида деления с остатком.
    """

    p, q = 1, 0
    r, s = 0, 1

    while not(a == 0 or b == 0):
        if b < a:
            k = a // b
            a -= k * b
            p -= k * r
            q -= k * s
        else:
            k = b // a
            b -= k * a
            r -= k * p
            s -= k * q

    if a == 0:
        return b, r, s

    return a, p, q


if __name__ == '__main__':

    import random

    num_tests = random.randrange(1, 1000, 1)
    random_values = []

    for __ in range(num_tests):
        random_values.append((random.randrange(1, 10000, 1), random.randrange(1, 10000, 1)))

    print('Check', num_tests, 'examples...')

    for i in random_values:
        assert sh_1_1_16(i[0], i[1])[1] * i[0] + sh_1_1_16(i[0], i[1])[2] * i[1] == sh_1_1_16(i[0], i[1])[0]

    print('Done!')
