# Time:  O(mn)
# Space: O(mn)

# 解题思路：
# 先考虑使用回溯，还是LTE
# 还是用动态规划，障碍物的dp为0


class Solution:
    # backtracking
    def uniquePathsWithObstacles1(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        count = 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        def uniquePathsR(x, y):
            nonlocal count
            if x == m - 1 and y == n - 1:
                count += 1
                return

            if x < m - 1 and not obstacleGrid[x + 1][y]:
                uniquePathsR(x + 1, y)
            if y < n - 1 and not obstacleGrid[x][y + 1]:
                uniquePathsR(x, y + 1)

        uniquePathsR(0, 0)

        return count

    # dp
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for i in range(n):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]

