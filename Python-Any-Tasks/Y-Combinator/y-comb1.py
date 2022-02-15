def fact(n):
    return n * fact(n-1) if n > 0 else 1


if __name__ == "__main__":
    print(fact(10))
