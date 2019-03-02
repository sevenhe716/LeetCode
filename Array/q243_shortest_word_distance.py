# Time:  O(n)
# Space: O(1)

# 解题思路：
# 可以用字典缓存索引，然后判断两个索引列表中的最小距离，核心问题就在于如何高效的找到两个列表中的最小差值，缓存的目的是多次调用效率更高
# 也可以one-pass遍历来完成

from collections import defaultdict


class Solution:
    def shortestDistance(self, words: 'List[str]', word1: str, word2: str) -> int:
        word_idx = defaultdict(list)
        for i, w in enumerate(words):
            word_idx[w] += [i]

        idx1, idx2 = word_idx[word1], word_idx[word2]
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
        return min_dist


class Solution1:
    def shortestDistance(self, words: 'List[str]', word1: str, word2: str) -> int:
        min_dist = len(words)
        # cur_word同时表示word1和word2，巧妙的做法
        cur_word, idx = None, 0
        for i, w in enumerate(words):
            if w not in (word1, word2):
                continue
            if cur_word and w != cur_word:
                min_dist = min(min_dist, i - idx)
            cur_word, idx = w, i
        return min_dist
