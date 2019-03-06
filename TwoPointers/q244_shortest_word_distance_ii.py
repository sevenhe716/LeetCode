# Time:  O(n)
# Space: O(1)

# 解题思路：
# 很明显需要增加预处理，来为多次调用提速
from collections import defaultdict


class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word_idx = defaultdict(list)
        for i, w in enumerate(words):
            self.word_idx[w] += [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1, idx2 = self.word_idx[word1], self.word_idx[word2]
        i1, i2 = 0, 0
        min_dist = abs(idx1[i1] - idx2[i2])

        while i1 < len(idx1) and i2 < len(idx2):
            while i1 < len(idx1) and idx1[i1] < idx2[i2]:
                i1 += 1
            min_dist = min(min_dist, abs(idx1[i1 - 1] - idx2[i2]))
            if i1 == len(idx1):
                return min_dist
            while i2 < len(idx2) and idx2[i2] < idx1[i1]:
                i2 += 1
            min_dist = min(min_dist, abs(idx2[i2 - 1] - idx1[i1]))
            if i2 == len(idx2):
                return min_dist
        # 这种写法更concise and clear
        # while l1 < len(loc1) and l2 < len(loc2):
        #     min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
        #     if loc1[l1] < loc2[l2]:
        #         l1 += 1
        #     else:
        #         l2 += 1
        # return min_diff
        return min_dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)