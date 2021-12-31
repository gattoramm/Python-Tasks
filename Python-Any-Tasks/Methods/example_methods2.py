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


from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)
    
    @staticmethod
    def is_adult(age):
        return age > 18


if __name__ == "__main__":
    person1 = Person('Sarah', 15)
    person2 = Person.from_birth_year('Roark', 2004)

    print(person1.name, person1.age)
    print(person2.name, person2.age)

    print(Person.is_adult(25))
