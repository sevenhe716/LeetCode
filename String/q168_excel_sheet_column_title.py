# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    # iteratively
    def convertToTitle1(self, n: 'int') -> 'str':
        res = ''
        while n > 0:
            k = (n - 1) % 26
            res = chr(ord('A') + k) + res
            if k == 25:
                n = n // 26 - 1     # 向上借一位
            else:
                n = n // 26
        return res

    # recursively
    def convertToTitle(self, n: 'int') -> 'str':
        if n <= 0:
            return ''
        k = (n - 1) % 26
        if k == 25:         # 向上借位
            return self.convertToTitle(n // 26 - 1) + chr(ord('A') + k)
        else:
            return self.convertToTitle(n // 26) + chr(ord('A') + k)
