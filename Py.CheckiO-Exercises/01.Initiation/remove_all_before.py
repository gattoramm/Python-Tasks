def remove_all_before(items, border):
    """
        Нужно удалить из список все элементы до указаного.
        Входные данные: Список и элемент до которого нужно удалить другие элементы.
        Выходные данные: Набор значений (кортеж, список, итератор ...).
    """
    if border in items:
        return items[items.index(border):]
    return items


if __name__ == '__main__':
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
