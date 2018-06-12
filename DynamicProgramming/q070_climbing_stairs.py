# Time:  O(n)
# Space: O(1)

# 解题思路：
# dp是一个比较常规的思路，dp[i] = dp[i-1] + dp[i-2]
# 优化思路：空间复杂度可以降为O(1)，只维护前两个指针即可


class Solution:
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp1 = dp2 = 1
        for i in range(n-1):
            dp2, dp1 = dp1 + dp2, dp2
        return dp2


