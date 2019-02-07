# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
