import random
import time
from functools import reduce

def test_zip_sum():
    arr = [random.random() for _ in range(1000)]
    total = 0
    start1 = time.time()

    for _ in range(10000):
        total += sum(a - b for a, b in zip(arr[1:], arr[:-1]) if a - b > 0)

    end1 = time.time()

    print("time=%d, result=%d", end1 - start1, total)

    start2 = time.time()

    total = 0
    for _ in range(10000):
        for i in range(len(arr) - 1):
            total += arr[i + 1] - arr[i] if arr[i + 1] - arr[i] > 0 else 0

    end2 = time.time()

    print("time2=%d, result=%d", end2 - start2, total)


def test_three_oper(a, b):
    return a - b if a - b > 0 else 0

def test_slice():
    arr = [1, 2, 3, 4, 5]
    slice = arr[:3]
    slice.reverse()
    print(slice)
    print(arr)

def test_sum():
    a1 = [1, 2]
    a2 = [2, 3, 4]
    # print(sum([a1, a2], key=len))
    print(reduce(lambda x, y: x + len(y), [a1, a2], 0))

def test_ret():
    if False:
        return 1

def test_print_sep():
    arr = [1, 2, 3, 4]
    print(*arr, sep='->')

def test():
    # test_sum()
    # print(test_ret())
    # test_print_sep()
    print((1, 2) + (2, 3))

if __name__ == '__main__':
    test()
