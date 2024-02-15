def func_inner(word='param=word in def func_inner'):
    if word is None:
        return 'param=word in def func_inner'
    elif len(word) == 0:
        return "Nothing"
    else:
        return word


if __name__ == "__main__":
    a1 = func_inner()
    a2 = func_inner("1")
    a3 = func_inner("")

    print(a1)
    print(a2)
    print(a3)
