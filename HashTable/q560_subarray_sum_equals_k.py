# Time:  O(n)
# Space: O(n)

# Ideas:
# sub_sum minus, space trade for time
# maintain the dict when traverse
from collections import defaultdict


class Solution:
    # 其实不需要维护list，计数即可
    def subarraySum(self, nums: 'List[int]', k: int) -> int:
        subsum_dict = defaultdict(list)
        subsum_dict[0].append(0)
        sub_sum, res = 0, 0
        for i, num in enumerate(nums):
            sub_sum += nums[i]
            if sub_sum - k in subsum_dict:
                res += len(subsum_dict[sub_sum-k])
            subsum_dict[sub_sum].append(i)

        return res


class Solution1:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        count, cur_sum = 0, 0
        mapping = defaultdict(int)
        mapping[0] = 1
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum-k in mapping:
                count += mapping[cur_sum-k]
            mapping[cur_sum] += 1
        return count