# Time:  O(n)
# Space: O(1)

# Ideas:
# mark divide and conquer
# if sub sum is negative just skip previous


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        sub_sum, max_sum = 0, float('-inf')
        for num in nums:
            max_sum = max(max_sum, sub_sum + num)
            sub_sum = max(0, sub_sum + num)
        return max_sum
