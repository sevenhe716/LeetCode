# Time:  O(mn)
# Space: O(1)

# 解题思路：
# 回溯，标记已访问过的节点


class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> int:
        if not grid:
            return 0
        m, n, res = len(grid), len(grid[0]), 0

        def backtrack(i, j):
            grid[i][j] = '*'
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                backtrack(i - 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                backtrack(i, j - 1)
            if i + 1 < m and grid[i + 1][j] == '1':
                backtrack(i + 1, j)
            if j + 1 < n and grid[i][j + 1] == '1':
                backtrack(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    backtrack(i, j)
                    res += 1
        return res


class Solution1:
    # 更简洁的写法
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1))
                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

# 并查集
class Solution2:
    def is_valid(self, grid, r, c):
        m, n = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        uf = UnionFind(grid)

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for d in directions:
                        nr, nc = i + d[0], j + d[1]
                        if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                            uf.union(i * n + j, nr * n + nc)
        return uf.count
