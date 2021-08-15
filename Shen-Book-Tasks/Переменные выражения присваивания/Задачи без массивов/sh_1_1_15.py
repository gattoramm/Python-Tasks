def sh_1_1_15(a: int, b: int) -> (int, int, int):
    """
        Вычисление d=НОД(a,b) и целых x и y,что d=a·x+b·y.
    """

    p, q = 1, 0
    r, s = 0, 1
    d = x = y = 0

    while not(a == 0 or b == 0):
        if b < a:
            a -= b
            p -= r
            q -= s
        else:
            b -= a
            r -= p
            s -= q

    if a == 0:
        d = b
        x = r
        y = s

    if b == 0:
        d = a
        x = p
        y = q

    return d, x, y


if __name__ == '__main__':

    import random

    num_tests = random.randrange(1, 1000, 1)
    random_values = []

    for __ in range(num_tests):
        random_values.append((random.randrange(1, 10000, 1), random.randrange(1, 10000, 1)))

    print('Check', num_tests, 'examples...')

    for i in random_values:
        assert sh_1_1_15(i[0], i[1])[1] * i[0] + sh_1_1_15(i[0], i[1])[2] * i[1] == sh_1_1_15(i[0], i[1])[0]

    print('Done!')
