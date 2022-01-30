def is_even(num: int) -> bool:
    """
        Проверить является ли число четным или нет.
        Входные данные: Целое число.
        Выходные данные: Логический тип.
    """
    return num & 1 == 0


if __name__ == '__main__':
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
