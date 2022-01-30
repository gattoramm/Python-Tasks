def get_talk(my_type="shout"):
    def shout(word="yes"):
        return word

    def whisper(word="no"):
        return word

    return shout if my_type == "shout" else whisper


if __name__ == "__main__":
    talk = get_talk()
    whisper = get_talk("whisper")
    print(talk)
    print(whisper)
    print("-----")
    print(talk())
    print(whisper())
    print("-----")
    print(get_talk("shout")())
    print(get_talk("whisper")())
