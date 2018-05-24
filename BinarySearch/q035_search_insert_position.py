# Time:  O(log(n))
# Space: O(1)

# 解题思路：
# 即bisect_left，二分查找，升序左插入


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)
        if target <= nums[lo]:
            return lo
        if target > nums[hi-1]:
            return hi

        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:  # 左插入应该与左侧比较
                lo = mid + 1
            else:
                hi = mid

        return lo