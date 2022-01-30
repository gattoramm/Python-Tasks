def beginning_zeros(number: str) -> int:
    """
        Дана строка состоящая только из цифр.
        Нужно посчитать сколько нулей ("0") находится в начале строки.
        Входные данные: Строка, состоящая только из цифр.
        Выходные данные: Целое число.
    """
    q = 0
    if number[0] == '0':
        for i in number:
            if i == '0':
                q += 1
            else:
                break
    return q


def beginning_zeros2(number: str) -> int:
    return len(number) - len(number.lstrip('0'))


if __name__ == '__main__':
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4

    assert beginning_zeros2('100') == 0
    assert beginning_zeros2('001') == 2
    assert beginning_zeros2('100100') == 0
    assert beginning_zeros2('001001') == 2
    assert beginning_zeros2('012345679') == 1
    assert beginning_zeros2('0000') == 4
