def sh_1_1_9rec(n: int) -> int:
    """
        Вычисление последовательности Фибоначчи рекурсивно с запоминанием
    """

    A = {0: 0, 1: 1}

    if n in A:
        return A[n]

    A[n] = sh_1_1_9rec(n - 1) + sh_1_1_9rec(n - 2)

    return A[n]


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_9rec(1) == 1
    assert sh_1_1_9rec(0) == 0
    assert sh_1_1_9rec(4) == 3
    assert sh_1_1_9rec(15) == 610
    assert sh_1_1_9rec(10) == 55

    print('Done!')
