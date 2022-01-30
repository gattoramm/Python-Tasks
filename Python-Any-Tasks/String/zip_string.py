"""
    Напишите программу, которая считывает строку, кодирует её
    алгоритмом и выводит закодированную последовательность на
    стандартный вывод. Кодирование должно учитывать регистр символов.

    Кодирование осуществляется следующим образом:
    s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы
    одинаковых символов исходной строки заменяются на этот символ и
    количество его повторений в этой позиции строки.
"""


def zip_string(input_string: str):
    input_string += ' '
    count = 0
    curr = input_string[0]
    for i in input_string:
        if curr != i:
            print(curr + str(count), end='')
            count = 0
            curr = i
        count += 1


if __name__ == '__main__':
    line = input()
    print("input_string:")
    zip_string(line)
