def sum_of_neighbors(input_list: list):
    """
        Напишите программу, на вход которой подаётся список чисел одной строкой.
        Программа должна для каждого элемента этого списка вывести сумму двух
        его соседей. Для элементов списка, являющихся крайними, одним из соседей
        считается элемент, находящий на противоположном конце этого списка.
    """
    if len(input_list) == 1:
        print(input_list[0])
    else:
        for i in range(len(input_list)):
            print(input_list[i - 1] + input_list[(i + 1) % len(input_list)], end=' ')


if __name__ == '__main__':
    a = [int(i) for i in input().split(' ')]
    print("sum_of_neighbors:")
    sum_of_neighbors(a)
