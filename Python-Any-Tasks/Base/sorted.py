def sorted(a: int, b: int, c: int):
    """
        Напишите программу, которая получает на вход три целых числа,
        по одному числу в строке, и выводит на консоль в три строки
        сначала максимальное, потом минимальное, после чего
        оставшееся число.
        На ввод могут подаваться и повторяющиеся числа.
    """
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        c, b = b, c
    print(a, c, b, sep='\n')


if __name__ == '__main__':
    a, b, c = int(input()), int(input()), int(input())
    print("output min, max, other:")
    sorted(a, b, c)
