from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    """
        Перед вами список целых чисел. Ваша задача в этой миссии – продублировать
        (..., 🍩, ... --> ..., 🍩, 🍩, ...)
        все нули в данном списке и вернуть в виде любого итерируемого объекта
    """

    return sum([[i] if i else [0, 0] for i in donuts], [])


if __name__ == "__main__":
    print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))
