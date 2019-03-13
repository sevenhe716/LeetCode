# Time:  O(n)
# Space: O(1)

# 解题思路：
# 异或之后统计1的个数，但对于python的负数应该如何处理？


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        print(bin(z))
        cnt = 0
        while z != 0:
            z = z & (z - 1)
            cnt += 1
        return cnt

class Solutio1:
    def hammingDistance(self, x: 'int', y: 'int') -> 'int':
        return bin(x ^ y).count('1')