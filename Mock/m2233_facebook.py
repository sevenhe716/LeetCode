# Time:  O(n)
# Space: O(1)

# Ideas:
# BFS
from collections import defaultdict


class Solution:
    def letterCombinations(self, digits: str) -> 'List[str]':
        if not digits:
            return []
        digit_letter = defaultdict(list)
        start = 0
        for i in range(2, 10):
            count = 4 if i == 7 or i == 9 else 3
            for j in range(count):
                digit_letter[str(i)].append(chr(ord('a') + start + j))
            start += count

        res = ['']
        for d in digits:
            res = [s + l for s in res for l in digit_letter[d]]
        return res