"""
    одна функция может вернуть другую функцию
"""

def talk():
    def whisper(word='yes'):
        return word
    
    print(whisper())

if __name__ == "__main__":
    talk()