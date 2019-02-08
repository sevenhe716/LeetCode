# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> 'bool':
        return len(set(nums)) != len(nums)
