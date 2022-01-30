def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    """Максимально общий декоратор"""
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Что нибудь передали?")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments


class Mary(object):

    def __init__(self):
        self.age = 31
    
    @a_decorator_passing_arbitrary_arguments
    # Теперь мы можем указать значение по умолчанию
    def say_your_age(self, lie=-3):
        print("Мне %s, а ты бы сколько дал?" % (self.age + lie))


if __name__ == "__main__":
    @a_decorator_passing_arbitrary_arguments
    def function_with_no_argument():
        print("Python is cool, no argument here.")
    
    function_with_no_argument()
    print("---------------")


    @a_decorator_passing_arbitrary_arguments
    def function_with_arguments(a, b, c):
        print(a, b, c)
    
    function_with_arguments(1, 2, 3)
    print("---------------")


    @a_decorator_passing_arbitrary_arguments
    def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
        print("Любят ли %s, %s и %s утконосов? %s" % (a, b, c, platypus))
    
    function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")
    print("---------------")
    m = Mary()
    m.say_your_age()
