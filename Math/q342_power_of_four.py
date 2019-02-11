# Time:  O(n)
# Space: O(1)

# 解题思路：
# 4的幂问题可以用位运算来解决


class Solution:
    def isPowerOfFour(self, num: 'int') -> 'bool':
        if num < 1:
            return False
        # 2的幂
        if num & (num - 1) != 0:
            return False
        while num > 1:
            num >>= 2
        return num == 1


class Solution1:
    # bin str的长度来判断
    def isPowerOfFour(self, num: 'int') -> 'bool':
        return num > 0 and num & (num - 1) == 0 and len(bin(num)) % 2 != 0

class Solution2:
    # 位运算
    def isPowerOfFour(self, num: 'int') -> 'bool':
        return num & (num - 1) == 0 and num & 0x55555555 != 0