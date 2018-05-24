# Time:  O(n)
# Space: O(1)

# 解题思路：
# 如果我没有理解错题意的话，应该是指0-n中有且只有一个数missing，因此可以用求和公式与数组和相减即可得出


# sum
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)     # sum(range(len(nums)+1)) 值得借鉴


# bit manipulate,  a^b^b = a
class Solution1:
    def missingNumber(self, nums):
        xor = 0

        for i, e in enumerate(nums):
            xor = xor ^ i ^ e

        return xor ^ len(nums)
