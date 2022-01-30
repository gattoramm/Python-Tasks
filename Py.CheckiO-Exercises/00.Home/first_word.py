def first_word(text: str) -> str:
    """
        Дана строка и нужно найти ее первое слово.
        Входные параметры: Строка.
        Выходные параметры: Строка.
    """
    return text.replace(',', ' ').replace('.', ' ').split()[0]


if __name__ == '__main__':

    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
