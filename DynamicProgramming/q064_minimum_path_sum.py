# Time:  O(mn)
# Space: O(mn)

# 解题思路：
# 考虑用动态规划 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
# 优化思路：只需要维护一个维度即可，空间复杂度会降为O(n)


class Solution:
    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]

        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]

    # 借鉴并理解
    # one-dimension dp
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        dp = [0] + [2147483647] * (n - 1)

        for i in range(m):
            dp[0] = dp[0] + grid[i][0]
            print(dp[0])
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]
