# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def titleToNumber(self, s: 'str') -> 'int':
        base, res = 1, 0
        for c in s[::-1]:
            res += base * (ord(c) - ord('A') + 1)
            base *= 26

        return res