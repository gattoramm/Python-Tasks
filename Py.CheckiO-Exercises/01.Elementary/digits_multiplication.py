def checkio(number: int) -> int:

    sum = 1

    while number > 0:
        if number%10 == 0:
            sum *= 1
        else:
            sum *= number%10
        number //= 10

    return sum


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
