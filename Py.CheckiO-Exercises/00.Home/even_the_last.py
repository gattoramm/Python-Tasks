def even_the_last(array: list) -> int:
    """
         Дан массив целых чисел. Нужно найти сумму элементов с четными индексами,
         затем перемножить эту сумму и последний элемент исходного массива.
         Входные данные: Список (list) целых чисел (int).
         Выходные данные: Число как целочисленное (int).
    """
    if len(array) == 0:
        return 0
    return sum(array[0::2]) * array[-1]


if __name__ == '__main__':

    assert even_the_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_the_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_the_last([6]) == 36, "(6)*6=36"
    assert even_the_last([]) == 0, "An empty array = 0"
