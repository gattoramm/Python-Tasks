def three_words(words: str) -> bool:
    """
        Дана строка со словами и числами, разделенными пробелами (один пробел между
        словами и/или числами). Слова состоят только из букв. Вам нужно проверить
        есть ли в исходной строке три слова подряд.
        Входные данные: Строка со словами (str).
        Выходные данные: Ответ как логическое выражение (bool), True или False.
    """
    i = 0
    for item in words.split():
        if not item.isdigit():
            i += 1
            if i > 2:
                return True
        else:
            i = 0
    return False


if __name__ == '__main__':
    assert three_words("Hello World hello") == True, "Hello"
    assert three_words("He is 123 man") == False, "123 man"
    assert three_words("1 2 3 4") == False, "Digits"
    assert three_words("bla bla bla bla") == True, "Bla Bla"
    assert three_words("Hi") == False, "Hi"
