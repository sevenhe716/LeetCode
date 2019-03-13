# Time:  O(RC)
# Space: O(RC)

# 解题思路：
# 记录完整的坐标，然后使用多种遍历方式去匹配，选择左上右上左下右下四个顶点，然后按照两个方向共计八个方向验证


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
    def numDistinctIslands2(self, grid: 'List[List[int]]') -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        islands = []

        dir = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

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