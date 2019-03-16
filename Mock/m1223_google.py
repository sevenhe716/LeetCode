# Time:  O(n)
# Space: O(1)

# Ideas:
# counter or dp
from collections import defaultdict


class Solution:
    def longestLine(self, M: 'List[List[int]]') -> int:
        if not M or not M[0]:
            return 0

        counter = defaultdict(int)
        max_len = 0
        for i, row in enumerate(M):
            for j, v in enumerate(row):
                for key in i+.1, j+.2, i+j+.3, i-j+.4:
                    if v == 1:
                        counter[key] += 1
                        max_len = max(max_len, counter[key])
                    else:
                        counter[key] = 0
        return max_len



