def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    begin_maker = text.index(begin) + 1
    end_maker = text.index(end)

    return text[begin_maker:end_maker]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')