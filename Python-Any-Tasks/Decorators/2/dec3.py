"""Декораторы класса"""


class CountCalls:
    def __init__(self, f):
        self.f = f
        self.called = 0

    def __call__(self, *args, **kwargs):
        self.called += 1
        return self.f(*args, **kwargs)


@CountCalls
def print_hello():
    print("hello")


print(print_hello.called)
print_hello()
print(print_hello.called)
