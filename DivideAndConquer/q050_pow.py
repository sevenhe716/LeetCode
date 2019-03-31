# Time:  O(n)
# Space: O(1)

# 解题思路：
# 指数按照二进制编码的方式处理即可
# 特殊情况：注意单独处理0的情况
# 优化思路：把除法转化成乘法


class Solution:
    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0:
            return 0

        base = x
        ans = 1
        positive = n > 0
        n = abs(n)

        while n != 0:
            if n & 1:
                ans = ans * base if positive else ans / base

            n >>= 1
            base *= base

        return ans

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0:
            return 0

        base = x if n > 0 else 1 / x
        ans = 1
        n = abs(n)

        while n != 0:
            if n & 1:
                ans = ans * base

            n >>= 1
            base *= base

        return ans


class Solution1:
    # divide and conquer
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n / 2)
