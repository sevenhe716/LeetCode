# Time:  O(n)
# Space: O(1)

# 解题思路：
# 观察数据，寻找规律，使用动态规划


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if not n or not k:
            return 0
        if n == 1:
            return k
        dp = [k, k * k]
        for i in range(2, n):
            dp.append(dp[-1] * (k - 1) + dp[-2] * (k - 1))
        return dp[-1]
