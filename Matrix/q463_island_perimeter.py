# Time:  O(mn)
# Space: O(1)

# 解题思路：
# 周长取决于1周围1的个数，0个1则为4，1个1则为3..4个1则为0
# 优化：如果左侧或上侧有相交的格子，则减去两条边


class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> int:
        m, n, res = len(grid), len(grid[0]), 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def check_island(i, j):
            return 1 if 0 <= i < m and 0 <= j < n and grid[i][j] == 1 else 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4 - sum(check_island(i + d[0], j + d[1]) for d in dirs)
        return res


# add 4 for each land and remove 2 for each internal edge
class Solution1:
    def islandPerimeter(self, grid):
        res = 0
        top = [0] * len(grid[0])  # surrounded by water (top)
        for row in grid:
            pre = 0  # surrounded by water (left)
            for i, cur in enumerate(row):
                if cur == 1:
                    res -= top[i] * 2  # minus 2 if there are dup edges on the top
                    if pre == 0:
                        res += 4  # (0 -> 1), add 4 (for new land)
                    else:
                        res += 2  # (1 -> 1), add 2 (4 new edges, but 2 are dup on the left)
                top[i], pre = cur, cur
        return res