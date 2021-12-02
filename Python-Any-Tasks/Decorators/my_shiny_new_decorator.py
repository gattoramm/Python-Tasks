"""
    Создадим свой декоратор «вручную»
"""
def my_shiny_new_decorator(a_function_to_decorate):

    def the_wrapper_around_the_original_function():
        # Поместим здесь код, который мы хотим запускать ДО вызова
        # оригинальной функции
        print("Я - код, который отработает до вызова функции")

        # ВЫЗОВЕМ саму декорируемую функцию
        a_function_to_decorate()

        # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова
        # оригинальной функции
        print ("А я - код, срабатывающий после")

    return the_wrapper_around_the_original_function


if __name__ == "__main__":
    def a_stand_alone_function():
        print("1")
    a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
    a_stand_alone_function()
    print("---------------")
    @my_shiny_new_decorator
    def another_stand_alone_function():
        print("Оставь меня в покое")
    another_stand_alone_function()