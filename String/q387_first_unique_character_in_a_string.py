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

class Solution1:
    # 只需要至多26*2次查找，充分利用了只包含小写字母的优势，find rfind相等即为唯一字符
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        res = len(s)
        for x in alphabet:
            index = s.find(x)
            if index == -1:
                continue
            if index == s.rfind(x):
                res = min(res, index)
        return -1 if res == len(s) else res