def sh_1_1_19(a: int, b: int) -> (int, int, int):
    """
        111
    """

    p, q = 1, 0
    r, s = 0, 1

    while not(a == 0 or b == 0):
        #if m % 2 == 0 and n % 2 == 0:
            #a //= 2
            #b //= 2

        if a % 2 == 0 and b % 2 == 0 and b < a:
            a /= 2
            b /= 2
            p -= 2 * r
            q -= 2 * s
        elif a % 2 == 0 and b % 2 == 0 and b >= a:
            k = b // a
            b -= k * a
            r -= k * p
            s -= k * q

    return 0, 0, 0