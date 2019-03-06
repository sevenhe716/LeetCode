# Time:  O(n)
# Space: O(1)

# 解题思路：
# Instead of using two-pointer, just use one pointer to represent both words, and same words case is also included.


class Solution:
    def shortestWordDistance(self, words: 'List[str]', word1: str, word2: str) -> int:
        cur_word, idx, min_dist = None, 0, len(words)
        for i, w in enumerate(words):
            if w not in (word1, word2):
                continue
            if cur_word and (word1 == word2 or w != cur_word):
                min_dist = min(min_dist, i - idx)
            cur_word, idx = w, i
        return min_dist
