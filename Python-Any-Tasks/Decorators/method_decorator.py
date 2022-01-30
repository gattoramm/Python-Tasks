def method_friendly_decorator(method_to_decorate):
    """Декорирование методов"""

    def wrapper(self, lie):
        lie = lie - 3
        return method_to_decorate(self, lie)

    return wrapper


class Lucy(object):
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def say_your_age(self, lie):
        print(self.age + lie)


if __name__ == "__main__":
    param = Lucy()
    param.say_your_age(-1)
