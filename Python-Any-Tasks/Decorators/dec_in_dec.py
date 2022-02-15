def decorator_maker():
    print("BEFORE my_decorator")
    def my_decorator(func):
        print("IN my_decorator")
        print("BEFORE wrapped")
        def wrapped():
            print("IN wrapped")
            return func()
        print("AFTER wrapped")
        return wrapped
    print("AFTER my_decorator")
    return my_decorator


if __name__ == "__main__":
    print("-------------------0")
    new_decorator = decorator_maker()
    print("-------------------1")
    def decorated_function():
        print("Я - декорируемая функция.")
    decorated_function = new_decorator(decorated_function)
    print("-------------------2")
    decorated_function()
