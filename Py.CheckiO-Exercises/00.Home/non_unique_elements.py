from collections.abc import Iterable
from collections import Counter


def non_unique_elements(array: list) -> Iterable[int]:
    """
         Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив, состоящий только из
         неуникальных элементов данного массива. Для этого необходимо удалить все уникальные элементы
         (которые присутствуют в данном массиве только один раз). Для решения этой задачи не меняйте
         оригинальный порядок элементов. Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и
         результат будет [1, 3, 1, 3].
    """

    freq = dict()
    for _ in array:
        if _ not in freq:
            freq[_] = 1
        else:
            freq[_] += 1

    res = list()
    for _ in array:
        if freq[_] != 1:
            res.append(_)

    return res


def non_unique_elements2(array: list) -> Iterable[int]:
    return [item for item in array if Counter(array)[item] > 1]


if __name__ == '__main__':
    assert list(non_unique_elements2([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
    assert list(non_unique_elements2([1, 2, 3, 4, 5])) == []
    assert list(non_unique_elements2([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
    assert list(non_unique_elements2([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
