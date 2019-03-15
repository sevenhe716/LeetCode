# Time:  O(RC)
# Space: O(RC)

# 解题思路：
# 在遍历过程中，把坐标记录起来，然后新的island需要跟老的island对比是否有重复
# 对比的方式，由于起始点和遍历顺序是一致的，可以直接对比对应的坐标即可
# 优化：使用hash与set可以加速比较的过程


class IslandPos:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return IslandPos(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return IslandPos(self.x - other.x, self.y - other.y)

    def __str__(self):
        return self.x + ', ' + self.y

    def __repr__(self):
        return "{},{}".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Solution:
    def numDistinctIslands(self, grid: 'List[List[int]]') -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        islands = []

        def backtrack(i, j, island):
            # 把坐标push到一个set中
            grid[i][j] = 0
            island.append(IslandPos(i, j))
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                backtrack(i - 1, j, island)
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                backtrack(i, j - 1, island)
            if i + 1 < m and grid[i + 1][j] == 1:
                backtrack(i + 1, j, island)
            if j + 1 < n and grid[i][j + 1] == 1:
                backtrack(i, j + 1, island)

        def check_unique(island):
            for cur_island in islands:
                if len(cur_island) != len(island):
                    continue
                offset = cur_island[0] - island[0]

                if all(cur_island[i] == island[i] + offset for i in range(1, len(island))):
                    return False
            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island = []
                    backtrack(i, j, island)
                    # check unique
                    if check_unique(island):
                        islands.append(island)
        return len(islands)


class Solution1:
    def numDistinctIslands(self, grid):
        seen = set()
        def explore(r, c, r0, c0):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add((r - r0, c - c0))
                explore(r+1, c, r0, c0)
                explore(r-1, c, r0, c0)
                explore(r, c+1, r0, c0)
                explore(r, c-1, r0, c0)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c, r, c)
                if shape:
                    shapes.add(frozenset(shape))
        return len(shapes)