# Time:  O(RC)
# Space: O(RC)

# 解题思路：
# 记录完整的坐标，然后使用多种遍历方式去匹配，选择左上右上左下右下四个顶点，然后按照两个方向共计八个方向验证


class Solution:
    def numDistinctIslands2(self, grid: 'List[List[int]]') -> int:
        if not grid:
            return 0
        m, n, islands = len(grid), len(grid[0]), []
        dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        def dfs(i, j, island):
            island.add((i, j))
            grid[i][j] = 0
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                dfs(i - 1, j, island)
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                dfs(i, j - 1, island)
            if i + 1 < m and grid[i + 1][j] == 1:
                dfs(i + 1, j, island)
            if j + 1 < n and grid[i][j + 1] == 1:
                dfs(i, j + 1, island)

        def check_unique(anchor1, anchor2, dir, island, cur_island, reverse):
            for pos in island:
                offset = ((pos[0] - anchor1[0]) * dir[0], (pos[1] - anchor1[1]) * dir[1])
                if reverse:
                    pos2 = (offset[1] + anchor2[0], offset[0] + anchor2[1])
                else:
                    pos2 = (offset[0] + anchor2[0], offset[1] + anchor2[1])

                if pos2 not in cur_island:
                    return True
            return False

        def check_uniques(island):
            anchors1, anchors2 = [], []
            for dir in dirs:
                anchors1.append(min(island, key=lambda x: (x[0] * dir[0], x[1] * dir[1])))
                anchors2.append(min(island, key=lambda x: (x[1] * dir[1], x[0] * dir[0])))

            # left_up = min(island, key=lambda x: (x[0], x[1]))
            # right_up = min(island, key=lambda x: (x[0], -x[1]))
            # left_down = min(island, key=lambda x: (-x[0], x[1]))
            # right_down = min(island, key=lambda x: (-x[0], -x[1]))
            #
            # left_up2 = min(island, key=lambda x: (x[1], x[0]))
            # right_up2 = min(island, key=lambda x: (-x[1], x[0]))
            # left_down2 = min(island, key=lambda x: (x[1], -x[0]))
            # right_down2 = min(island, key=lambda x: (-x[1], -x[0]))

            for cur_island in islands:
                if len(cur_island) != len(island):
                    continue

                cur_anchor = min(cur_island, key=lambda x: (x[0], x[1]))
                for dir, anchor1, anchor2 in zip(dirs, anchors1, anchors2):
                    if not check_unique(anchor1, cur_anchor, dir, island, cur_island, False):
                        return False
                    if not check_unique(anchor2, cur_anchor, dir, island, cur_island, True):
                        return False
            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island = set()
                    dfs(i, j, island)
                    # check unique
                    if check_uniques(island):
                        islands.append(island)
        return len(islands)


class Solution1:
    def numDistinctIslands21(self, grid):
        seen = set()
        def explore(r, c):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add(complex(r, c))
                explore(r+1, c)
                explore(r-1, c)
                explore(r, c+1)
                explore(r, c-1)

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape),
                            min(z.imag for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = []
            for k in range(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans,  translate([complex(z.imag, z.real) * (1j)**k
                                           for z in shape]))
            return tuple(ans)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c)
                if shape:
                    shapes.add(canonical(shape))

        return len(shapes)

    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])

        # augment matrix to void length check
        grid.append([0] * n)
        for row in grid: row.append(0)

        self.pool = set()
        self.res = 0

        def bfs(i0, j0):
            grid[i0][j0] = -1
            q = [(i0, j0)]
            # 借鉴list边遍历边修改的写法
            for i, j in q:
                for I, J in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if grid[I][J] == 1:
                        grid[I][J] = -1
                        q.append([I, J])
            self.addisland(q)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: bfs(i, j)

        return self.res

    def addisland(self, q):
        Imin = min(x for x, y in q)
        Jmin = min(y for x, y in q)
        island1 = tuple(sorted((x - Imin, y - Jmin) for x, y in q))  # original island

        if island1 in self.pool: return None
        self.res += 1

        Imax = max(x for x, y in island1)
        Jmax = max(y for x, y in island1)

        island2 = tuple(sorted((-x + Imax, y) for x, y in island1))  # x axis mirror
        island3 = tuple(sorted((x, -y + Jmax) for x, y in island1))  # y axis mirror
        island4 = tuple(sorted((-x + Imax, -y + Jmax) for x, y in island1))  # origin mirror

        island5 = tuple(sorted((y, x) for x, y in island1))  # diagonal mirror
        island6 = tuple(sorted((-x + Jmax, y) for x, y in island5))
        island7 = tuple(sorted((x, -y + Imax) for x, y in island5))
        island8 = tuple(sorted((-x + Jmax, -y + Imax) for x, y in island5))

        self.pool |= set([island1, island2, island3, island4, island5, island6, island7, island8])