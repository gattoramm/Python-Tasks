def talk():
    """Одна функция может вернуть другую функцию"""
    def whisper(word='yes'):
        return word
    
    print(whisper())


if __name__ == "__main__":
    talk()
