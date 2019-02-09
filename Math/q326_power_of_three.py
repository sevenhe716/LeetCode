# Time:  O(n)
# Space: O(1)

# 解题思路：
# 不用循环或递归如何解决？
# 很tricky的做法，用大于int32作为检测的被除数
# 或者是用log，注意精度损失


class Solution:
    def isPowerOfThree(self, n: 'int') -> 'bool':
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


class Solution1:
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0