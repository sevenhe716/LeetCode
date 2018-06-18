# Time:  O(n) O(log(n))
# Space: O(1)

# 解题思路：
# 题意理解上有分歧，有且认为只有一个波峰，且不是以降序开始的，我的理解是寻找第一个波峰
# 因为只有一个波峰，也可以考虑用二分查找


class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        up = False

        for i in range(len(A) - 1):
            if up:
                if A[i] > A[i + 1]:
                    return i
            else:
                if A[i] < A[i + 1]:
                    up = True

        return -1


class Solution1:
    # linear search
    def peakIndexInMountainArray(self, A):
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                return i

    # binary search
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A)
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
