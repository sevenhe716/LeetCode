# Time:  O(nlogn)
# Space: O(n)

# Ideas:
#
from bisect import bisect_left


class Solution:
    # dp
    def lengthOfLIS1(self, nums: 'List[int]') -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

    # dp with binary search
    def lengthOfLIS(self, nums: 'List[int]') -> int:
        dp = [0] * len(nums)

        length = 0
        for num in nums:
            i = bisect_left(dp, num, 0, length)
            if i < 0:
                i = -(i + 1)
            dp[i] = num
            if i == length:
                length += 1
        return length
