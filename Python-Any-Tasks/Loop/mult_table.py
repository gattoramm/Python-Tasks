def mult_table(a: int, b: int, c: int, d: int):
    """
    Напишите программу, на вход которой даются четыре числа a, b, c и d,
    каждое в своей строке. Программа должна вывести фрагмент таблицы
    умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка
    [c;d][c;d].
    Числа a, b, c и d являются натуральными и не превосходят 10, a
    a≤b, c≤d.
    """
    print('', *range(c, d + 1), sep='\t')
    for i in range(a, b + 1):
        print(i, *range(i * c, (i * d) + 1, i), sep='\t')


if __name__ == '__main__':
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    print("table:")
    mult_table(a, b, c, d)
