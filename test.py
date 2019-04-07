import random
import time
from functools import reduce
from collections import Counter
from collections import deque
import heapq
from itertools import islice


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


def test_for():
    a = [1, 2, 3, 4]
    for i, v in enumerate(a):
        a.append(1)
        a.append(2)
        print(i, v)


def test_slice():
    # 倒排索引
    print((1, 2)[-1::-1])
    # 支持索引越界
    a = [0, 1, 2, 3]
    print(a[4:])


def test_slice_assign():
    arr = [1, 2, 4, 2]
    # 允许不等长，可以多赋值或少赋值
    arr[1:3] = [0]
    print(arr)


# 允许直接删除某元素
def test_arr_del():
    arr = [1, 2, 4, 2]
    del arr[2]
    print(arr)


# 当counter计数为0时，依然在counter中
def test_counter():
    cnt = Counter({2: 1})
    print(1 in cnt)
    print(2 in cnt)
    cnt[2] -= 1
    print(2 in cnt)
    print(cnt[2])


def test_set_edit_traverse():
    s = [1, -1]
    for i in s:
        s.append(i+1)
        print(i)
        if i > 10:
            return

def test_mix_list():
    a = [1] + [1.1]
    print(type(a[0]))
    print(type(a[1]))

def test_inf():
    print(0 - float('inf'))

def test_and():
    print(3 and 5)
    print(None and 5)
    print(3 and None)

def test_mutilple_assign():
    nums = [2, 0, 1]
    tmp = nums[0]
    nums[0], nums[tmp] = nums[tmp], nums[0]     # nums=[1, 0, 2] right
    print(nums)
    nums = [2, 0, 1]
    nums[nums[0]], nums[0] = nums[0], nums[nums[0]] # nums=[1, 2, 1] wrong
    print(nums)
    nums = [2, 0, 1]
    nums[0], nums[2] = nums[2], nums[0] # nums=[1, 2, 1] wrong
    print(nums)

def test_siftup():
    data = [10, 5, 18, 2, 37, 3, 8, 7, 19, 1]
    heapq.heapify(data)
    print(data)
    old, new = 3, 100  # increase the 8 to 22
    i = data.index(old)
    data[i] = new
    heapq._siftup(data, 0, i)
    print(data)

def test_islice():
    n = 3
    iter = iter(range(n ** 2))
    board = [list(islice(iter, n)) for _ in range(n)]
    print(board)

def postorder_traversal_iteratively(root: 'TreeNode'):
    if not root:
        return []
    stack = [root]
    # used to record whether left or right child has been visited
    last = None

    while stack:
        root = stack[-1]
        # if current node has no left right child, or left child or right child has been visited, then process and pop it
        if not root.left and not root.right or last and (root.left == last or root.right == last):
            '''
            add current node logic here
            '''
            print(root.val)

            stack.pop()
            last = root
        # if not, push right and left child in stack
        else:
            # push right first because of FILO
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

from common import TreeNode

def test():
    # test_sum()
    # print(test_ret())
    # test_print_sep()
    # test_slice()
    # test_arr_del()
    # a = arr[::-1]
    # a.remove(2)
    # print(a[::-1])
    # a = '0000'
    # print(a[2:2].startswith('0'))
    # print('123'.ljust(5, '0'))
    # s = 'L321e2t1C1o1d1e1'
    # s.split('')
    # test_counter()
    # test_set_edit_traverse()
    # test_mix_list()
    # queue = deque()
    # queue.append(1)
    # queue.append(2)
    # queue.append(3)
    # a = [1]
    # print(a[-2::-1])
    # print('00 11 88 69 96'.split())
    # print(int(True))
    # for i in range(10):
    #     print(i)
    # s = 'abc  abe'
    # print(s.split())
    # print(-2 % 26)
    # print(sorted((3, 1, 2)))
    # test_inf()
    # print([1] + [0]*-2)
    # test_and()
    # test_mutilple_assign()
    # counter = Counter('abc')
    # # counter['d'] -= 1
    # print(counter['a'])
    # print(counter['d'])
    # print('d' in counter)

    # postorder_traversal_iteratively(TreeNode.generate([1, 2, 3, 4, 5, 6, 7]))

    s = 'abcab'

    print(','.join(s))

if __name__ == '__main__':
    test()
