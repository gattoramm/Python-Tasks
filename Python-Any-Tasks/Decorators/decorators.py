def dec(foo=None):
    print('in dec')
    return foo


def func(n: int = 100) -> int:
    return n


@dec
def func2(n: int = 200) -> int:
    return n


if __name__ == "__main__":
    # print("Декорируем функцию в функцию без @: ", dec(5))
    print("Декорируем функцию в функцию через @: ", func2())
