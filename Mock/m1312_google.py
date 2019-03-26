# Time:  O(n)
# Space: O(n)

# Ideas:
# dict version union-find

# Using union-find with rank and path compression.
#
# Time Complexity Calculations: Total Number of operations=(N+P). Number of
# nodes=2*P Thus time complexity=O((N+P)* alpha(P)) alpha(P) (Also know as
# Inverse-Ackermann function) grows very slowly and will always be less than or
# equal to 4.


class Union:
    def __init__(self, value):
        self.v = value
        self.root = self
        self.rank = 0


class UnionFind:
    # path compress and rank
    def __init__(self):
        self.us = {}

    def create_union(self, value):
        u = Union(value)
        self.us[u.v] = u
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
        if x_root.rank < y_root.rank:
            x_root.root = y_root
        elif x_root.rank > y_root.rank:
            y_root.root = x_root
        else:
            x_root.root = y_root
            y_root.rank += 1


class Solution:
    def areSentencesSimilarTwo(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        if len(words1) != len(words2):
            return False
        union_set = UnionFind()

        def is_connected(w1, w2):
            if w1 not in union_set.us or w2 not in union_set.us:
                return w1 == w2
            return union_set.find(union_set.us[w1]) == union_set.find(union_set.us[w2])

        for pair in pairs:
            for w in pair:
                if w not in union_set.us:
                    union_set.create_union(w)

        for w1, w2 in pairs:
            union_set.union(union_set.us[w1], union_set.us[w2])
        return all(is_connected(w1, w2) for w1, w2 in zip(words1, words2))
