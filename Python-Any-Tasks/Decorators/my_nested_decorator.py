def bread(func):
    """Можно вкладывать декораторы друг в друга."""
    def wrapper():
        print("</----------\>")
        func()
        print("<\__________/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print("##помидоры##")
        func()
        print("~~салат~~")

    return wrapper


def sandwich(food="--ветчина--"):
    print(food)


if __name__ == "__main__":
    sandwich()
    print("@@@@@@@@@@@@@@@@@@@")
    sandwich = bread(ingredients(sandwich))
    sandwich()
    print("через декоратор @")


    @bread
    @ingredients
    def sandwich(food="--ветчина--"):
        print(food)


    sandwich()
    print("изменен порядок следования декораторов")


    @ingredients
    @bread
    def sandwich(food="--ветчина--"):
        print(food)


    sandwich()
