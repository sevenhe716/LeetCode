# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        num_dict = {}
        for i, n in enumerate(nums):
            if target - n in num_dict:
                return [num_dict[target - n], i]
            else:
                num_dict[n] = i
        return []

