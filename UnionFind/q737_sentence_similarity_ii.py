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


# 并查集的另一种写法，映射到整数的数组
class DSU:  # DSU 类适用于所有union find 的问题
    def __init__(self, n):  # n 选一个足够大的数即可。
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        self.parent[p_x] = p_y


class Solution1:
    def areSentencesSimilarTwo(self, words1, words2, pairs):

        if len(words1) != len(words2):
            return False
        i = 0  # 每个word的id
        word2id = {}  # word -> ID

        dsu = DSU(2 * len(pairs))  # 大小下限是 unique word in pairs， 没有上限，可以选择任意大的数

        for w1, w2 in pairs:
            if w1 not in word2id:  # 建立映射
                word2id[w1] = i
                i += 1
            if w2 not in word2id:
                word2id[w2] = i
                i += 1
            dsu.merge(word2id[w1], word2id[w2])  # 两个word在同一个pair里，把两个id merge即可

        for w1, w2 in zip(words1, words2):
            if w1 == w2:  # Corner case: 单词本身跟自己相似，不管他们在不在pairs 表里。
                continue
            if not w1 in word2id or not w2 in word2id:  # Corner case: words1 和words2里的单词可能不在pairs 表里，表示他们不可能跟其他单词有相似关系。
                return False
            if dsu.find(word2id[w1]) != dsu.find(word2id[w2]):  # 只要判断两个单词的id 是否指向共同的parent
                return False
        return True