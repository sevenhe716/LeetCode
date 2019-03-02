# Time:  O(n)
# Space: O(n)

# 解题思路：
# 构造支持颠倒数字的map，先判断是否有其他数字，再映射之后翻转，与原字符串比较
# 优化：空间复杂度O(1)的做法，直接遍历数组进行比较，而不是构造一个字符串
import operator


class Solution:
    # 构造了一个新的字符串，空间复杂度为O(n)
    def isStrobogrammatic1(self, num: str) -> bool:
        strob_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        if any(w not in strob_map.keys() for w in num):
            return False
        s = map(lambda x: strob_map[x], num)
        return num == ''.join(s)[::-1]

    def isStrobogrammatic(self, num: str) -> bool:
        strob_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        return all(strob_map.get(c1, '') == c2 for c1, c2 in zip(num, num[::-1]))


# one-line pythonic的写法
# https://leetcode.com/problems/strobogrammatic-number/discuss/67203/1-liners-Python
class Solution1:
    def isStrobogrammatic(self, num):
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num) // 2 + 1))

    def isStrobogrammatic1(self, num):
        return all(c + d in '696 00 11 88' for c, d in zip(num, num[::-1]))

    def isStrobogrammatic2(self, num):
        return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)))

    def isStrobogrammatic3(self, num):
        return all(map('696 00 11 88'.count, map(operator.add, num, num[::-1])))

    def isStrobogrammatic4(self, num):
        return all(p in '696 00 11 88' for p in map(operator.add, num, num[::-1]))

    def isStrobogrammatic5(self, num):
        return set(map(operator.add, num, num[::-1])) <= set('69 96 00 11 88'.split())

    def isStrobogrammatic6(self, num):
        return set(map(operator.add, num, num[::-1])) <= {'69', '96', '00', '11', '88'}

    def isStrobogrammatic7s(self, num):
        return set(map(''.join, zip(num, num[::-1]))) <= {'69', '96', '00', '11', '88'}
