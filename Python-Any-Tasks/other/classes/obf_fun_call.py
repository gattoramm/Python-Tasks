class Greeting(object):
    def __init__(self, greeting='hello'):
        self.greeting = greeting

    def greet(self, name):
        return '%s! %s' % (self.greeting, name)

def greet2(name):
        ob = Greeting('hola')
        print(ob.greet('bob'))
        return


greeting = Greeting('hola')
print(greeting.greet('bob'))
print()
print(greet2('bob'))
