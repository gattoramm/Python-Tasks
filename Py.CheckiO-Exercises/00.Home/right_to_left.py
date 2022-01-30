def right_to_left(phrases):
    """
        Дана строка со словами и числами, разделенными пробелами (один пробел
        между словами и/или числами). Слова состоят только из букв. Нужно
        проверить есть ли в исходной строке три слова подряд.
        Входные данные: Строка со словами (str).
        Выходные данные: Ответ как логическое выражение (bool), True или False.
    """
    result = ",".join(phrases).replace('right', 'left')
    return result


if __name__ == '__main__':
    assert right_to_left(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert right_to_left(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert right_to_left(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert right_to_left(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
