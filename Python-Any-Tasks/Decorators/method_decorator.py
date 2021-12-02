"""
    Декорирование методов
"""
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3
        return method_to_decorate(self, lie)
    return wrapper

class Lucy(object):

    def __init__(self):
        self.age = 32
    
    @method_friendly_decorator
    def sayYourAge(self, lie):
        print(self.age + lie)

if __name__ == "__main__":
    l = Lucy()
    l.sayYourAge(-1)