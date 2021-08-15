def sh_1_1_1(a: int, b: int) -> (int, int):
    """
        Меняет местами 2 входных параметра
    """

    tmp = a
    a = b
    b = tmp
    return a, b


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_1(2, 5) == (5, 2)
    assert sh_1_1_1(5, -8) == (-8, 5)
    assert sh_1_1_1(-3, -4) == (-4, -3)
    assert sh_1_1_1(0, 0) == (0, 0)

    print('Done!')
