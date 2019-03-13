# Time:  O(n)
# Space: O(1)

# 解题思路：
# sqrt，判断另一个数是否为整数
# 二分查找
import math


class Solution:
    # c >= 0
    def judgeSquareSum1(self, c: int) -> bool:
        a, a_2 = 0, 0
        while a_2 <= c:
            b = int(math.sqrt(c - a_2))
            if b * b == c - a_2:
                return True
            a += 1
            a_2 = a * a
        return False

    # 二分查找
    def judgeSquareSum(self, c: int) -> bool:
        def is_sqrt(num):
            lo, hi, mid = 0, num, 0
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if mid * mid == num:
                    return True
                elif mid * mid < num:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return mid * mid == num

        return any(is_sqrt(c - a * a) for a in range(int(c ** 0.5) + 1))


class Solution1:
    # more pythonic
    def judgeSquareSum(self, c):
        def is_square(N):
            return int(N ** .5) ** 2 == N

        return any(is_square(c - a * a) for a in range(int(c ** .5) + 1))
