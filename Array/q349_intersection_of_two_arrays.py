# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        return list(set(nums1).intersection(set(nums2)))