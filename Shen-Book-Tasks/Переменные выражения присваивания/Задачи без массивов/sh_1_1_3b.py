def sh_1_1_3b(a: int, n: int) -> int:
    """
        Вычисление a^n.
    """

    k, b = n, 1
    while k != 0:
        b *= a
        k -= 1
    return b


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_3b( 2, 5) == 2**5
    assert sh_1_1_3b( 5, 2) == 5**2
    assert sh_1_1_3b( 3, 4) == 3**4
    assert sh_1_1_3b(45645, 0) == 45645**0
    assert sh_1_1_3b( sh_1_1_3b(2, 3), 2) == (2**3)**2

    print('Done!')
