def sh_1_1_3(a: int, n: int) -> int:
    """
        Вычисление a^n.
    """

    k, b = 0, 1

    while k < n:
        b *= a
        k += 1
    return b


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_3(2, 5) == 2**5
    assert sh_1_1_3(5, 2) == 5**2
    assert sh_1_1_3(3, 4) == 3**4
    assert sh_1_1_3(45645, 0) == 45645**0
    assert sh_1_1_3(sh_1_1_3(2, 3), 2) == (2**3)**2

    print('Done!')
