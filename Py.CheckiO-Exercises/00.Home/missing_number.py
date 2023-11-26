def missing_number(items: list[int]) -> int:
    """
        Вам дана последовательность целых чисел, являющаяся элементами арифметической прогрессии — разница
        между последовательными элементами постоянна. Но эта последовательность не отсортирована и один
        элемент отсутствует.
    """

    items.sort()

    for i in range(len(items)//2):
        delta_l, delta_r = items[i+1] - items[i], items[-i-1] - items[-i-2]

        if delta_l > delta_r:
            return items[i] + delta_r
        if delta_l < delta_r:
            return items[-i-2] + delta_l

    return 0


if __name__ == '__main__':
    print(missing_number([1, 4, 2, 5]))
    # assert missing_number([1, 4, 2, 5]) == 3
    # assert missing_number([2, 6, 8]) == 4
