def fuzzbuzz(n)->str:
    result = ""
    if n%3 == 0:
        result += "fuzz"
    if n%5 == 0:
        result += "buzz"
    return result

import sys

if __name__ == "__main__":
    for _ in range(1, 116):
        print(f"n = {_},\tfuzzbuz? - {fuzzbuzz(_)}")
