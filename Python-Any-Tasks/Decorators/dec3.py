def do_smth_before(func):
    """Можно передавать функцию другой функции, как параметр"""
    print(func())


def shout(word="yes"):
    return word


scream = shout


if __name__ == "__main__":
    do_smth_before(scream)
