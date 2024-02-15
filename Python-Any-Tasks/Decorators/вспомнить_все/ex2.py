def func_outer(param1):
    def func_inner1(param='**yes**'):
        print("--------in func_inner1--------")
        return param + param1

    def func_inner2(param='**no**'):
        print("--------in func_inner2--------")
        return param + param1

    return func_inner1 if param1 is None else func_inner2


if __name__ == "__main__":
    print('                 func_outer()()')
    print('result =', func_outer()())
    print('                 func_outer("1")()')
    print('result =', func_outer("1")())
    print('                 func_outer()("2")')
    print('result =', func_outer()("2"))
    print('                 func_outer("3")("1")')
    print('result =', func_outer("3")("1"))
