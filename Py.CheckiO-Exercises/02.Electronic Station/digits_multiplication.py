def digits_multiplication(number: int) -> int:
    """
        Дано положительное целое число. Необходимо подсчитать
        произведение всех цифр в этом числе, за исключением нулей.
        Входные данные: Положительное целое число.
        Выходные данные: Произведение цифр как целочисленное (int).
    """
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res


if __name__ == '__main__':
    assert digits_multiplication(123405) == 120
    assert digits_multiplication(999) == 729
    assert digits_multiplication(1000) == 1
    assert digits_multiplication(1111) == 1
