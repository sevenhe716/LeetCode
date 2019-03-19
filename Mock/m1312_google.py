# Time:  O(n)
# Space: O(1)

# Ideas:
# dict version union-find


class Union:
    def __init__(self, x):
        self.root = x


class UnionSet:
    # add is_rank
    def __init__(self):
        self.us = {}

    def make_union_set(self, pairs):
        for pair in pairs:
            for w in pair:
                if w not in self.us:
                    self.us[w] = Union(w)

    def find(self, word):
        # x = self.us[word]
        x = word
        cur = self.us[x]
        while self.us[x].root != x:
            x = self.us[x].root
        root = x
        # path compress
        while cur.root != root:
            cur, cur.root = self.us[cur.root], root
        return root

    def union(self, w1, w2):
        self.us[self.find(w1)].root = self.find(w2)

    def is_connected(self, w1, w2):
        if w1 not in self.us or w2 not in self.us:
            return w1 == w2
        return self.find(w1) == self.find(w2)


class Solution:
    def areSentencesSimilarTwo(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        if len(words1) != len(words2):
            return False
        union_set = UnionSet()
        union_set.make_union_set(pairs)
        for w1, w2 in pairs:
            union_set.union(w1, w2)
        return all(union_set.is_connected(w1, w2) for w1, w2 in zip(words1, words2))
