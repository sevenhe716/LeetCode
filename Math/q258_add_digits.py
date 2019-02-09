# Time:  O(n)
# Space: O(1)

# 解题思路：
# 不使用循环和递归，用O(1)的时间解决
# Math Problem
# The problem, widely known as digit root problem, has a congruence formula:
# https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
# ~input: 0 1 2 3 4 ...
# output: 0 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 ....

class Solution:
    def addDigits(self, num: 'int') -> 'int':
        while num > 9:
            total = 0
            while num:
                num, r = divmod(num, 10)
                total += r
            num = total
        return num


class Solution1(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num - 1) % 9 + 1 if num != 0 else 0
