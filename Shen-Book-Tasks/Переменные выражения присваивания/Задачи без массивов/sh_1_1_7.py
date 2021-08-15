def sh_1_1_7(a: int, d: int) -> (int, int):
    """
        Вычисление частного q и остатка r при делении
        а (целое неотрицательное) на d (целое положительное),
        не используя операций div и mod.
    """

    r, q = a, 0
    while r >= d:
        r -= d
        q += 1

    return q, r

if __name__ == '__main__':

    import random

    num_tests = random.randrange(1, 1000, 1)
    random_values = []

    for __ in range(num_tests):
        random_values.append((random.randrange(1, 10000, 1), random.randrange(1, 10000, 1)))

    print('Check', num_tests, 'examples...')

    for i in random_values:
        assert sh_1_1_7(i[0], i[1])  == (i[0] // i[1], i[0] % i[1])

    print('Done!')
