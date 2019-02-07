# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def isHappy(self, n: 'int') -> 'bool':
        def calHappyNum(num):
            res = 0
            while num > 0:
                num, r = divmod(num, 10)
                res += r * r
            return res
        nums = set()
        while n not in nums:
            nums.add(n)
            n = calHappyNum(n)
            if n == 1:
                return True
        return False

class Solution1:
    def isHappy(self, n):
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True