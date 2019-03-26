# Time:  O(n)
# Space: O(n)

# Ideas:
# sub sum and minus
# mark
from collections import defaultdict


class Solution:
    def maxSubArrayLen(self, nums: 'List[int]', k: int) -> int:
        sub_sums = defaultdict(list)
        sub_sums[0].append(0)
        total = 0
        for i, num in enumerate(nums):
            total += num
            sub_sums[total].append(i + 1)

        res = 0
        # 比较麻烦的是处理相等的情况
        for key, val in sub_sums.items():
            for v1 in val:
                if key - k in sub_sums:
                    for v2 in sub_sums[key - k]:
                        res = max(res, v1 - v2)
        return res


class Solution1:
    def maxSubArrayLen(self, nums, k):
        ans, acc = 0, 0  # answer and the accumulative value of nums
        mp = {0: -1}  # key is acc value, and value is the index
        for i in range(len(nums)):
            acc += nums[i]
            # 如果mp中已经存在了，则只需要保留最短的，也就是第一个，这样就解决了重复的问题
            if acc not in mp:
                mp[acc] = i
            if acc - k in mp:
                ans = max(ans, i - mp[acc - k])
        return ans
