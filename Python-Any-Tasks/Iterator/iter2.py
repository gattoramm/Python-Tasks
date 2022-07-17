class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <= 5:
            return index * 2
        else:
            raise IndexError


if __name__ == '__main__':
    iterable = SimpleIterable()
    for value in iterable:
        print(value)
