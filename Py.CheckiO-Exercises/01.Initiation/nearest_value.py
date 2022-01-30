def nearest_value(values: set, one: int) -> int:
    """
        Найдите ближайшее значение к переданному.
        Входные данные: Два аргумента. Ряд значений в виде set.
            Искомое значение - int
        Выходные данные: Int.
    """
    new_val = []
    new_val_diff = []
    values = sorted(values)
    for i in values:
        new_val.append(i)
    for i in new_val:
        new_val_diff.append(abs(one - i))
    r = min(new_val_diff)
    for i in range(len(new_val_diff)):
        while new_val_diff[i] == r:
            return new_val[i]
    return r


def nearest_value2(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))


if __name__ == '__main__':
    assert nearest_value({0, -2}, -1) == -2
    assert nearest_value({4, 7, 10, 11, 12, 17}, 10) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
