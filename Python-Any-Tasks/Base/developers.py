def developer(n: int):
    """
         Напишите программу, считывающую с пользовательского ввода
         целое число n (неотрицательное до 1000 включительно),
         выводящее это число в консоль вместе с правильным образом
         изменённым словом "программист", например: 1 программист,
         2 программиста, 5 программистов.
    """
    if n % 10 == 1 and n % 100 != 11:
        print(str(n) + " программист")
    if n % 10 in (2, 3, 4) and n % 100 not in range(12, 20):
        print(str(n) + " программиста")
    if n % 10 in (0, 5, 6, 7, 8, 9) or n % 100 in range(11, 20):
        print(str(n) + " программистов")


if __name__ == '__main__':
    a = int(input())
    print("counts of developers:")
    developer(a)
