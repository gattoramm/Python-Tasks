def correct_sentence(text: str) -> str:
    """
        На вход функции будет передано одно предложение.
        Необходимо вернуть его исправленную копию так, чтобы оно
        всегда начиналось с большой буквы и заканчивалось точкой.
        Входные аргументы: Строка (A string).
        Выходные аргументы: Строка (A string).
    """
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")


if __name__ == '__main__':
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
