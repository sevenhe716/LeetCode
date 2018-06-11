# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 动态规划，T(n)记录到当前的最少Jump次数，可以选择往前求解或者往后求解，往前求解时间复杂度固定为O(n*(n-1)/2)
# 往后求解时间复杂度最坏情况下是O(n*(n-1)/2)
# 优化思路：观察规律可得知，若前一个元素已覆盖的区域，后一个元素无需再重复遍历，而是往当前索引继续向后遍历即可，时间复杂度降低到O(n)


class Solution:
    def jump1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [n] * n
        dp[0] = 0

        for i in range(n):
            for j in range(1, min(nums[i] + 1, n - i)):
                dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[n - 1]

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        cur = 0  # 标记当前遍历位置

        for i in range(n):
            for j in range(max(1, cur + 1 - i), min(nums[i] + 1, n - i)):
                dp[i + j] = dp[i] + 1
                cur = i + j

        return dp[n - 1]
