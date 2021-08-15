def sh_1_1_8rec(n: int) -> int:
    """
        Вычисление n! методом рекурсии
    """

    if n != 0:
        return n * sh_1_1_8rec( n - 1 )
    return 1


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_8rec( 1 ) == 1
    assert sh_1_1_8rec( 0 ) == 1
    assert sh_1_1_8rec( 3 ) == 6
    assert sh_1_1_8rec( 5 ) == 120
    assert sh_1_1_8rec( 10 ) == 3628800

    print('Done!')
