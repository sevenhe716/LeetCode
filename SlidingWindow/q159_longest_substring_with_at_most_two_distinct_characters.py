# Time:  O(n)
# Space: O(1)

# 解题思路：
# substring template
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = defaultdict(int)
        count, start, end, res = 0, 0, 0, 0
        while end < len(s):
            if counter[s[end]] == 0:
                count += 1
            counter[s[end]] += 1
            end += 1
            while count > 2:
                if counter[s[start]] == 1:
                    count -= 1
                counter[s[start]] -= 1
                start += 1
            res = max(res, end - start)
        return res
