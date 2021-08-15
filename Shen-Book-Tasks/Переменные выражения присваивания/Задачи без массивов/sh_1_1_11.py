def sh_1_1_11(n: int) -> float:
    """
        Вычисление 1/0! + 1/1! +...+ 1/n!
    """

    sum_ = 1.0

    for out_k in range(1, n + 1):
        mp = 1.0
        for in_k in range(1, out_k + 1):
            mp *= in_k
        sum_ += 1 / mp

    return sum_


if __name__ == '__main__':
    print('Check examples...')

    assert round( sh_1_1_11(1), 7) == 2.0
    assert round( sh_1_1_11(0), 7) == 1.0
    assert round( sh_1_1_11(4), 7) == 2.7083333
    assert round( sh_1_1_11(7), 7) == 2.718254
    assert round( sh_1_1_11(10), 7) == 2.7182818

    print('Done!')