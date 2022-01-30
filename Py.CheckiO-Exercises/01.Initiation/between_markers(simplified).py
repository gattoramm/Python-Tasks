def between_markers(text: str, begin: str, end: str) -> str:
    """
        Дана строка и два маркера (начальный и конечный).
        Необходимо найти текст, заключенный между двумя этими маркерами.
        Входные данные: Три аргумента. Все строки. Второй и третий
            аргументы это начальный и конечный маркеры.
        Выходные данные: Строка.
    """
    begin_maker = text.index(begin) + 1
    end_maker = text.index(end)
    return text[begin_maker:end_maker]


if __name__ == '__main__':
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
