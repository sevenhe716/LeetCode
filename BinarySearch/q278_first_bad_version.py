# Time:  O(logn)
# Space: O(1)

# 解题思路：
# 二分查找，快速定位问题


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n, val):
        """
        :type n: int
        :rtype: int
        """

        def isBadVersion(version):
            return version >= val

        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid
        return low


def isBadVersion(version):
    return version >= 1


class Solution1:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                # 右边界也减1，通过left <= right来保证left返回正确，让二分搜索次数更少
                right = mid - 1
            else:
                left = mid + 1
        return left
