# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def isPowerOfTwo(self, n: 'int') -> 'bool':
        if n <= 0:
            return False
        return n & (n - 1) == 0
