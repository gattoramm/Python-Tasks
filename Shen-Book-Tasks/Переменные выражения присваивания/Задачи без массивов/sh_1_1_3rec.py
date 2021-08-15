def sh_1_1_3_rec(a: int, n: int) -> int:
    """
        Вычисление a^n методом рекурсии
    """

    if n != 0:
        return a * sh_1_1_3_rec(a, n - 1)
    return 1


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_3_rec(2, 5) == 2**5
    assert sh_1_1_3_rec(5, 2) == 5**2
    assert sh_1_1_3_rec(3, 4) == 3**4
    assert sh_1_1_3_rec(45645, 0) == 45645**0
    assert sh_1_1_3_rec(sh_1_1_3_rec(2, 3), 2) == (2**3)**2

    print('Done!')
