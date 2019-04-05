# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution(object):
    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

    def hammingWeight(self, n):
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count