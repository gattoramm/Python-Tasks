def sh_1_1_2(a: int, b: int) -> (int, int):
    """
        Меняет местами 2 входных параметра, без дополнительных переменных
    """

    a += b
    b = a - b
    a -= b
    return a, b


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_2(2, 5) == (5, 2)
    assert sh_1_1_2(5, -8) == (-8, 5)
    assert sh_1_1_2(-3, -4) == (-4, -3)
    assert sh_1_1_2(0, 0) == (0, 0)

    print('Done!')
