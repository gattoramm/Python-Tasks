def sh_1_1_9(n: int) -> int:
    """
        Вычисление последовательности Фибоначчи
    """

    a0, a1 = 0, 1

    while n > 0:
        a0, a1 = a1, a1 + a0
        n -= 1
    return a0


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_9(1) == 1
    assert sh_1_1_9(0) == 0
    assert sh_1_1_9(4) == 3
    assert sh_1_1_9(15) == 610
    assert sh_1_1_9(10) == 55

    print('Done!')
