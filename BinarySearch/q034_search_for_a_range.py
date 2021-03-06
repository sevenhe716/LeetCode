# Time:  O(log(n))
# Space: O(1)

# 解题思路：
# 二分查找，即bisect_left, bisect_right，并且要相等


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        from bisect import bisect_left
        from bisect import bisect_right

        if not nums:
            return [-1, -1]

        left = bisect_left(nums, target)
        right = bisect_right(nums, target)

        if left >= len(nums) or nums[left] != target or nums[right - 1] != target:
            return [-1, -1]

        return [left, right - 1]

def searchRange2(self, nums: 'List[int]', target: int) -> 'List[int]':
    left = self.search_leftmost(nums, target)
    right = self.search_leftmost(nums, target + 1) - 1
    return [left, right] if target in nums[left:left + 1] else [-1, -1]

    def search_leftmost(self, nums, target) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo
