# Time:  O(n)
# Space: O(1)

# Ideas:
# union find's time complexity?


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