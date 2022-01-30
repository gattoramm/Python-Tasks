def backward_string(val: str) -> str:
    """
        Верните данную строку в перевернутом виде.
        Входные данные: Строка.
        Выходные данные: Строка.
    """
    return val[::-1]


if __name__ == '__main__':
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
