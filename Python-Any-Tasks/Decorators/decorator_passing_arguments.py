def a_decorator_passing_arguments(function_to_decorate):
    """Передача («проброс») аргументов в декорируемую функцию"""
    def a_wrapper_accepting_arguments(arg1, arg2):
        function_to_decorate(arg1, arg2)
        print("Wow", arg1, arg2)
    return a_wrapper_accepting_arguments


if __name__ == "__main__":
    @a_decorator_passing_arguments
    def print_full_name(first_name, last_name):
        print("Меня зовут", first_name, last_name)
    
    print_full_name("Питер", "Венкман")
