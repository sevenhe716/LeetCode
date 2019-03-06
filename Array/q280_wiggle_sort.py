# Time:  O(n)
# Space: O(1)

# 解题思路：
# nlog(n)的解法是比较容易想到的，但是有没有更快的办法
# 尝试one-pass O(n)的greedy方案


class Solution:
    def wiggleSort(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            # if i % 2 == 1 and nums[i] < nums[i+1] or i % 2 == 0 and nums[i] > nums[i+1]:
            # 这个写法更简洁
            if i % 2 == (nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


class Solution:
    def wiggleSort(self, nums):
        # neat, brilliant and beautiful trick
        for i in range(len(nums)):
            nums[i:i + 2] = sorted(nums[i:i + 2], reverse=i % 2)
