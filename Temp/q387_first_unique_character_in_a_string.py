# Time:  O(n)
# Space: O(1)

# 解题思路：
#
from collections import Counter


class Solution:
    # 计数器解法
    def firstUniqChar1(self, s: 'str') -> 'int':
        cnt = Counter(s)

        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

    # index dict
    def firstUniqChar(self, s: 'str') -> 'int':
        pos = {}
        for i, c in enumerate(s):
            if c in pos:
                pos[c] = -1
            else:
                pos[c] = i

        for i, c in enumerate(s):
            if pos[c] != -1:
                return pos[c]
        return -1
