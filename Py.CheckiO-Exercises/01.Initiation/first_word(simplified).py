def first_word(text: str) -> str:
    """
        Дана строка и нужно найти ее первое слово.
        Строка состоит только из английских символов и пробелов.
        В начале и в конце строки пробелов нет.
        Входные параметры: Строка.
        Выходные параметры**: Строка.
    """
    return text.replace(',', ' ').split()[0]


if __name__ == '__main__':
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
