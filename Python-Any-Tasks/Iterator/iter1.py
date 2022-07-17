def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break


def loop_body(value):
    print('Next value:', value)


if __name__ == '__main__':
    my_for(range(10), loop_body)
