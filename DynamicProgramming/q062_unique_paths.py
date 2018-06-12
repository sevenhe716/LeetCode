# Time:  O(mn)
# Space: O(mn)

# 解题思路：
# 回溯寻找所有路径，但是TLE
# 考虑使用dp, 记录到达每一个格子产生的path, dp[i][j] = dp[i-1][j] + dp[i][j-1]
# 优化思路：只需要维护一个维度即可，空间复杂度会降为O(n)


class Solution:
    # backtracking
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 0

        def uniquePathsR(x, y):
            nonlocal count
            if x == m - 1 and y == n - 1:
                count += 1
                return

            if x < m - 1:
                uniquePathsR(x + 1, y)
            if y < n - 1:
                uniquePathsR(x, y + 1)

        uniquePathsR(0, 0)

        return count

    # dp
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]


# math way，mn和的阶乘除以m和n的阶乘
class SolutionF:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def f(n):
            ret = 1
            for i in range(1, n + 1):
                ret *= i
            return ret

        return f(m + n - 2) // (f(m - 1) * f(n - 1))

