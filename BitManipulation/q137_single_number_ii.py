# Time:  O(n)
# Space: O(1)

# Ideas:
# https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers


class Solution:
    def singleNumber(self, nums: 'List[int]') -> int:
        x1, x2 = 0, 0
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask
        return x1