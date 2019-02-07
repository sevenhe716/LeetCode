# Time:  O(n)
# Space: O(1)

# 解题思路：
#
from functools import reduce


class Solution:
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for n in nums:
            ret = ret ^ n

        return ret

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)