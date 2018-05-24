# Time:  O(log(n))
# Space: O(1)

# 解题思路：
# 除数的二进制加减法来表示
# 优化思路：无需缓存除数的list，直接从个数


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        divisors = [divisor]

        while divisors[-1] <= dividend:
            divisors.append(divisors[-1] << 1)

        i = len(divisors) - 1
        quotient = 0

        for i in range(len(divisors)-1)[::-1]:
            quotient <<= 1
            if dividend >= divisors[i]:
                dividend -= divisors[i]
                quotient += 1

        return -quotient if neg else min(quotient, 2147483647)


class SolutionF:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(res, 2147483647)
