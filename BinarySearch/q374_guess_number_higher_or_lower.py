# Time:  O(n)
# Space: O(1)

# 解题思路：
# 二分查找


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
import bisect
pick = 0


def guess(num):
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


# 三分查找，时间复杂度降为log3(2n)
class Solution1:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3
            res1, res2 = guess(mid1), guess(mid2)
            if res1 == 0:
                return mid1
            if res2 == 0:
                return mid2
            elif res1 < 0:
                high = mid1 - 1
            elif res2 > 0:
                low = mid2 + 1
            else:
                low, high = mid1 + 1, mid2 - 1
        return -1

    def guessNumber1(self, n):
        class C: __getitem__ = lambda _, i: -guess(i)
        return bisect.bisect(C(), -1, 1, n)
