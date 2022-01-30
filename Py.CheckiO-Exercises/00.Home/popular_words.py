def popular_words(text: str, words: list) -> dict:
    """
        Определить популярность определенных слов в тексте.
        Входные параметры: Текст и массив искомых слов.
        Выходные параметры: Словарь, в котором ключами являются искомые
        слова и значениями то, сколько раз они встречаются в исходном тексте.
    """
    lower_count = text.lower().split().count
    return {word: lower_count(word) for word in words}


if __name__ == '__main__':
    assert popular_words('''
        When I was One
        I had just begun
        When I was Two
        I was nearly new
        ''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
