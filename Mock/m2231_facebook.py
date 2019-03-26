# Time:  O(n^2)
# Space: O(1)

# Ideas:
# not contain duplicate triplets
# mark
from collections import defaultdict


class Solution:
    # TLE O(n^2)
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        two_sum_dict = defaultdict(list)

        result = set()
        for i, num in enumerate(nums):
            if -num in two_sum_dict:
                for v in two_sum_dict[-num]:
                    result.add(tuple(sorted((v[0], v[1], num))))
            for num2 in nums[:i]:
                two_sum_dict[num2+num].append((num2, num))

        return list(map(list, result))




