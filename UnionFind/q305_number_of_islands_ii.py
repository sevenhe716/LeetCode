# Time:  O(n)
# Space: O(n)

# Ideas:
# union find's time complexity?
# actually m, n are no use here


class Union:
    def __init__(self, value):
        self.v = value
        self.root = self
        self.rank = 0


class UnionFind:
    # path compress and rank
    def __init__(self):
        self.us = {}
        self.count = 0

    def create_union(self, value):
        u = Union(value)
        self.us[u.v] = u
        self.count += 1
        return u

    def find(self, x):
        cur = x

        while cur.root != cur:
            cur = cur.root
        root = cur
        while x.root != root:
            x, x.root, x.rank = x.root, root, 1
        return root

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.count -= 1
        if x_root.rank < y_root.rank:
            x_root.root = y_root
        elif x_root.rank > y_root.rank:
            y_root.root = x_root
        else:
            x_root.root = y_root
            y_root.rank += 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: 'List[List[int]]') -> 'List[int]':
        us = UnionFind()
        res = []
        for i, j in positions:
            new_island = us.create_union((i, j))
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n and (I, J) in us.us:
                    us.union(us.us[(I, J)], new_island)

            res.append(us.count)
        return res


class Solution1:
    def numIslands2(self, m: 'int', n: 'int', positions: 'List[List[int]]') -> 'List[int]':
        # 延展左右边界，兼容边界情况
        grid = [(n + 2) * [0] for i in range(m + 2)]
        fus = list(range(n * m))
        def find(x):
            if x == fus[x]:
                return x
            fus[x] = find(fus[x])
            return fus[x]
        conn = 0
        ans = []
        for x, y in positions:
            if not grid[x + 1][y + 1]:
                conn += 1
                grid[x + 1][y + 1] = 1
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if grid[x + 1 + dx][y + 1 + dy]:
                        r1 = find(x * n + y)
                        r2 = find((x + dx) * n + y + dy)
                        if r1 != r2:
                            fus[r1] = r2
                            conn -= 1
            ans += [conn]
        return ans

    # 借鉴stefan大神的union find写法
    def numIslands21(self, m, n, positions):
        parent, rank, count = {}, {}, 0

        def find(x):
            # find路径压缩时，不需要更新rank吗？
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            x, y = find(x), find(y)
            if x != y:
                if rank[x] < rank[y]:
                    x, y = y, x
                parent[y] = x
                rank[x] += rank[x] == rank[y]
                count -= 1

        def add(pos):
            nonlocal count
            i, j = pos
            x = parent[x] = i, j
            rank[x] = 0
            count += 1
            for y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if y in parent:
                    union(x, y)
            return count

        return list(map(add, positions))