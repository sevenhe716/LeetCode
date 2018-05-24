# Time:  O(n)
# Space: O(1)

# 解题思路：
# const空间 O(n)时间，虽然只能使用常数空间，nums本身具有O(n)空间，可以借用
# 把第i个数放在nums[i]索引的位置，然后再从头遍历，找到第一个nums[i]!=i的数即可


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] < n and nums[nums[i] - 1] != nums[i]:        # replace until all in place
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i, num in enumerate(nums):
            if i != num-1:
                return i + 1

        return n + 1
