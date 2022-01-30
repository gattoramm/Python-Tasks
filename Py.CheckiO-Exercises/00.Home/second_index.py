def second_index(text: str, symbol: str) -> [int, None]:
    """
        Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.
        Входные аргументы: Две строки (String)
        Выходные аргументы: Int or None
    """
    if text.count(symbol) < 2:
        return None
    return text.index(symbol, text.index(symbol) + 1)


if __name__ == '__main__':
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
