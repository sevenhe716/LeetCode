# Time:  O(n)
# Space: O(1)

# 解题思路：
# 把非零的值往前赋值，往前的步数取决于0的个数
# 题目要求的是最少操作次数，因此用双指针交换是更好的方式


class Solution:
    def moveZeroes1(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        step = 0
        for i, num in enumerate(nums):
            if num == 0:
                step += 1
            elif step > 0:
                nums[i - step] = num
        if step > 0:
            nums[-step:] = [0] * step

    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        last_nonzero_index = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[last_nonzero_index], nums[cur] = nums[cur], nums[last_nonzero_index]
                last_nonzero_index += 1


class Solution1:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = 0
        for n in nums:
            if n != 0:
                nums[i], i = n, i + 1

        for j in range(i, len(nums)):
            nums[j] = 0
