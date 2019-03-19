# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = '0'
            for I, J in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                if 0 <= I < m and 0 <= J < n and grid[I][J] == '1':
                    dfs(I, J)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res