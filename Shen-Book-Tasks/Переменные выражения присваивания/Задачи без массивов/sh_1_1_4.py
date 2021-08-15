def sh_1_1_4(a: int, n: int) -> int:
    """
        Вычисление a^n. Число действий порядка log(n).
    """

    k, b, c = n, 1, a
    while k != 0:
        if k % 2 == 0:
            k /= 2
            c *= c
        k -= 1
        b *= c
    return b


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_4(2, 5) == 2**5
    assert sh_1_1_4(5, 2) == 5**2
    assert sh_1_1_4(3, 4) == 3**4
    assert sh_1_1_4(45645, 0) == 45645**0
    assert sh_1_1_4(sh_1_1_4(2, 3), 2) == (2**3)**2

    print('Done!')
