# Time:  O(n)
# Space: O(1)

# 解题思路：
# 最后剩4个，且是后手，则能赢
# 1,5,9,13，先拿一个，必胜
# 2,6,10,14，先拿两个，必胜
# 3,7,11,15，先拿三个，必胜
# 4,8,12,16，最后4个是对面后手，必输


class Solution:
    def canWinNim(self, n: 'int') -> 'bool':
        return n % 4 != 0