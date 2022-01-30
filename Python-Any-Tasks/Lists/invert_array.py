def invert_array1(A: list, N: int):
    """
        Обращение массива (поворот задом-наперёд)
        в рамках индексов от 0 до N-1
    """
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]


def invert_array2(A: list, N: int):
    """
        Обращение массива (поворот задом-наперёд)
        в рамках индексов от 0 до N-1
        с помощью циклического сдвига влево
    """
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp


def test_invert_array(invert_array_algorithm):
    print("Тестируем:", invert_array_algorithm.__doc__)

    print("testcase #1: ", end="")
    A = [1, 2, 3333, -4, 55]
    A_invert = [55, -4, 3333, 2, 1]
    invert_array_algorithm(A, len(A))
    print("Ok" if A == A_invert else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_invert = list(range(9, -1, -1)) + list(range(19, 9, -1))
    invert_array_algorithm(A, len(A))
    print("Ok" if A == A_invert else "Fail")

    print("testcase #3: ", end="")
    A = [0, 0, 0, 0, 0, 0, 0, 10]
    A_invert = [10, 0, 0, 0, 0, 0, 0, 0]
    invert_array_algorithm(A, len(A))
    print("Ok" if A == A_invert else "Fail")


if __name__ == "__main__":
    test_invert_array(invert_array1)
    test_invert_array(invert_array2)

