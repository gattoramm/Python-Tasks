"""
Стоимость квартиры на первом этаже составляет X долларов.
Стоимость квартиры возрастает на 1000 долларов каждые M этажей.
N этажей
"""


def result(N: int = 30, X: int = 10000, M: int = 10) -> int:
    _t1 = N // M
    _t2 = N % M
    summator = 0

    for _ in range(_t1):
        summator += (X + 1000 * _) * M

    summator += (X + 1000 * (_t1 + 1)) * _t2
    return summator


def result2(N: int = 30, X: int = 10000, M: int = 10) -> int:
    return sum((X + 1000 * _) * M for _ in range(N // M)) + (X + 1000 * (N // M + 1)) * N % M


if __name__ == "__main__":
    a = result(50, 1000, 10)
    b = result2(50, 1000, 10)
    print(a)
    print(b)
