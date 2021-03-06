# Time:  O(log(n))
# Space: O(1)

# 解题思路：
# 颠倒叠加后判断是否与原数相等即可，更快的方式是直接转化成字符串翻转，但是有额外的空间复杂度，而且题目要求不转为字符串
# 特殊情况考虑：
# 1. 排除掉负数
# 2. 翻转后可能会溢出（其实不用考虑翻转后溢出的问题，因为python3整型精度无上限，若原数不溢出，而翻转后溢出，则两数必不相等）
# 优化思路：其实只用翻转一半即可，结束条件为原数小于翻转以后的数

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:               # 先排除负数，对于一半数据的时间复杂度可以从O(log(n))提高到O(1)
            return False

        y, _x = 0, x

        while _x > 0:
            _x, remain = divmod(_x, 10)
            # remain = _x % 10
            # _x = (_x - remain) // 10        # 直接 _x //= 10即可
            y = y * 10 + remain

        # 其实不用考虑翻转后溢出的问题，因为python3整型精度无上限，若原数不溢出，而翻转后溢出，则两数必不相等
        # if y > (1 << 31) - 1:
        #   return False

        return x == y


# 其实只用翻转一半即可，结束条件为原数小于翻转以后的数，判断 x == y or x == y // 10
class Solution1:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0 or x % 10 == 0 and x:
            return False

        revert = 0
        while x > revert:
            x, remain = divmod(x, 10)
            revert = revert * 10 + remain

        return x == revert or x == revert // 10

# 加减法也不如字符串翻转转int快
class SolutionF:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return int(str(x)[::-1]) == x
