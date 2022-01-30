def between_markers(text: str, begin: str, end: str) -> str:
    """
        Дана строка и два маркера (начальный и конечный). Необходимо найти текст,
        заключенный между двумя этими маркерами.
        Входные параметры: Три аргумента. Все строки. Второй и третий аргументы это
        начальный и конечный маркеры.
        Выходные параметры: Строка.
    """
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]


if __name__ == '__main__':
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>", "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
