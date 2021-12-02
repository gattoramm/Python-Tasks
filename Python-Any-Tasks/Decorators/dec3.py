"""
    можно передавать функцию другой функции, как параметр
"""

def doSmthBerore(func):
    print(func())

def shout(word="yes"):
    return word

scream = shout

if __name__ == "__main__":
    doSmthBerore(scream)