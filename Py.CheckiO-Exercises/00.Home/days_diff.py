from datetime import datetime


def days(a):
    if a[0] < 4:
        a[0] = '0' * (4 - len(a[0])) + a[0]
    return datetime.strptime('-'.join(map(str, a)), '%Y-%m-%d')


def days_diff(a, b):
    daystop = datetime.strptime('-'.join(map(str, a)), '%Y-%m-%d')
    daystart = datetime.strptime('-'.join(map(str, b)), '%Y-%m-%d')
    return abs((daystop - daystart).days)


if __name__ == "__main__":
    print(days((1000, 4, 19)))
