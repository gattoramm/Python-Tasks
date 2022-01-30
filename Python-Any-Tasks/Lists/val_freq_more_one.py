def val_freq_more_one(input_list: list):
    """
        Напишите программу, которая принимает на вход список чисел
        в одной строке через пробел и выводит на экран в одну строку
        значения, которые встречаются в нём более одного раза.
    """
    for _ in set(input_list):
        if input_list.count(_) > 1:
            print(_, end=' ')


def val_freq_more_one2(input_list: list):
    input_list = sorted(input_list)
    curr = input_list[0]
    count = 1
    for i in range(1, len(input_list)):
        if input_list[i] == curr:
            count += 1
            if i == len(input_list) - 1 and count > 1:
                print(curr, end=' ')
        else:
            if count > 1:
                print(curr, end=' ')
            count = 1
        curr = input_list[i]


if __name__ == '__main__':
    a = [int(i) for i in input().split(' ')]
    print("val_freq_more_one:")
    val_freq_more_one(a)
    print("val_freq_more_one2:")
    val_freq_more_one2(a)
