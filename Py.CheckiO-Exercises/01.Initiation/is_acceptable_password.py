def is_acceptable_password(password: str) -> bool:
    """
        Нужно создать функцию проверки пароля.
        Условия проверки: длина пароля должна быть больше 6.
        Входные данные: Строка.
        Выходные данные: Логический тип.
    """
    return len(password) > 6


if __name__ == '__main__':
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
