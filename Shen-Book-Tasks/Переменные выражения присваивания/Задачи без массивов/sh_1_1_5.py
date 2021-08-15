def sh_1_1_5(a: int, b: int) -> int:
    """
        Вычисление a * b (a и b - натуральные), используя лишь операции
        +, -, =, <>.
    """

    if a < b:
        a, b = b, a

    sum, k = 0, 0
    while k != b:
        sum += a
        k += 1
    return sum


if __name__ == '__main__':
    print('Check examples...')

    assert sh_1_1_5(2, 5) == 2 * 5
    assert sh_1_1_5(5, 2) == 5 * 2
    assert sh_1_1_5(3, 44) == 3 * 44
    assert sh_1_1_5(1, 8) == 1 * 8
    assert sh_1_1_5(4, 0) == 4 * 0
    assert sh_1_1_5(sh_1_1_5(2, 3), sh_1_1_5(2, 14 )) == (2 * 3) * (2 * 14)

    print('Done!')
