# Time:  O(log(n))
# Space: O(1)

# 解题思路：
# 比较简单的想法是，从1开始求平方，直到大于等于x
# 优化思路：底数平方或者double来加速接近解
# 优化思路：二分查找
# 优化思路：牛顿法 https://leetcode.com/problems/sqrtx/discuss/25057/3-4-short-lines-Integer-Newton-Every-Language


class Solution:
    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        for i in range(1, x + 1):
            product = i * i
            if product == x:
                return i
            elif product > x:
                return i - 1

    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        base = 1
        while base * base <= x:
            base <<= 1

        for i in range(base >> 1, x + 1):
            product = i * i
            if product == x:
                return i
            elif product > x:
                return i - 1

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 4:
            return 1

        base = 2
        base2 = base * base
        while base2 * base2 <= x:  # square jump
            base = base2
            base2 *= base2

        while base * base <= x:  # double jump
            base <<= 1

        for i in range(base >> 1, x + 1):
            product = i * i
            if product == x:
                return i
            elif product > x:
                return i - 1


class Solution1:
    # Binary search
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1

    # Newton's method
    def mySqrt(self, x):
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r
