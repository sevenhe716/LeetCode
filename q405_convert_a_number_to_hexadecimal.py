# Time:  O(n)
# Space: O(1)

# 解题思路：
# 负数为正数取反再加1
letter_map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


class Solution:
    def toHex(self, num: 'int') -> 'str':
        if num == 0:
            return '0'
        if num < 0:
            mask = int('ffffffff', 16)
            num = (mask ^ (-num)) + 1
        ans = ''
        while num > 0:
            num, r = divmod(num, 16)
            ans = letter_map[r] + ans
        return ans
