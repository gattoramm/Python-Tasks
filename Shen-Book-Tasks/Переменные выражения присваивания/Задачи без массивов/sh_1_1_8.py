def sh_1_1_8(n: int) -> int:
    """
        Вычисление n!.
    """

    m = 1

    for k in range(1, n + 1):
        m *= k

    return m


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_8(1) == 1
    assert sh_1_1_8(0) == 1
    assert sh_1_1_8(3) == 6
    assert sh_1_1_8(5) == 120
    assert sh_1_1_8(10) == 3628800

    print('Done!')
