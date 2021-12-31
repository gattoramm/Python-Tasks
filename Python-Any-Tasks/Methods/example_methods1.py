"""
    Методы экземпляра класса.
    Они позволяют менять как состояние определённого объекта, так и класса.
    
    Методы класса.
    Они могут менять состояние класса, что отразится на всех
    объектах этого класса, но не могут менять конкретный объект.

    Статические методы.
    Они прикреплены к классу лишь для удобства и не могут менять
    состояние ни класса, ни его экземпляра.
"""


class ToyClass:

    def instancemethod(self):
        return 'instance method called', self
    

    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    
    
    @staticmethod
    def staticmethod():
        return 'static method called'

if __name__ == "__main__":
    obj = ToyClass()

    # через объект класса:
    print("Через объект класса:")
    # instancemethod имеет доступ к объекту класса ToyClass через аргумент self
    print(obj.instancemethod())
    print(ToyClass.instancemethod(obj))

    # вызовем метод класса
    print(obj.classmethod())

    # вызовем статический метод:
    print(obj.staticmethod())

    # через сам класс
    print("Через сам класс:")
    print(ToyClass().instancemethod())
    print(ToyClass.classmethod())
    print(ToyClass().classmethod())
    print(ToyClass.staticmethod())
