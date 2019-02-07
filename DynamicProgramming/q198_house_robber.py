# Time:  O(n)
# Space: O(1)

# 解题思路：
# 先尝试用dp来解决，最多隔两个房子，dp[i] = max(dp[i-2], dp[i-3]) + nums[i]


class Solution:
    # 空间优化：只需两个即可
    def rob(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        if n < 3:
            return max(nums)
        dp = [0] * n
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, n):
            dp[i] = (dp[i-2] if dp[i-2] >= dp[i-3] else dp[i-3]) + nums[i]

        return max(dp[-1], dp[-2])

    def rob(self, nums: 'List[int]') -> 'int':
        dp1, dp2 = 0, 0
        for i in nums:
            dp1, dp2 = dp2, max(dp2, dp1+i)
        return dp2


class Solution1:
    def rob(self, nums: 'List[int]') -> 'int':
        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now