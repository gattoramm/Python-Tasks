def getTalk(type="shout"):

    def shout(word="yes"):
        return word

    def whisper(word="no"):
        return word

    return shout if type == "shout" else whisper


if __name__ == "__main__":
    talk = getTalk()
    whisper = getTalk("whisper")
    print(talk)
    print(whisper)
    print("-----")
    print(talk())
    print(whisper())
    print("-----")
    print(getTalk("shout")())
    print(getTalk("whisper")())