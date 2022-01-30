def fuzzbuzz(n: int) -> str:
    """
        Вывести вместо чисел, кратных 3 - слово "fuzz", а вместо чисел,
        кратных 5 — слово "buzz". Если число кратно 15, то Вывести слово
        "fuzzbuzz", в остальных случаях просто вывести число.
    """
    result = ""
    if n % 3 == 0:
        result += "fuzz"
    if n % 5 == 0:
        result += "buzz"
    if n % 3 != 0 and n % 5 != 0:
        result += str(n)
    return result


if __name__ == "__main__":
    for _ in range(1, 101):
        print(f"{fuzzbuzz(_)}")
