# Time:  O(n)
# Space: O(n)

# 解题思路：
# 实际这个问题是寻找最长子串，只包含两个字符，可以考虑sliding window?
from collections import defaultdict


class Solution:
    def totalFruit(self, tree: 'List[int]') -> int:
        cnt = defaultdict(int)
        count, start, end, res = 0, 0, 0, 0

        while end < len(tree):
            if cnt[tree[end]] == 0:
                count += 1
            cnt[tree[end]] += 1
            end += 1
            while count > 2:
                if cnt[tree[start]] == 1:
                    count -= 1
                cnt[tree[start]] -= 1
                start += 1
            res = max(res, end - start)
        return res


class Solution1:
    # 很喜欢这种解法，store current two element, and fastest
    def totalFruit(self, tree):
        res = cur = count_b = a = b = 0
        for c in tree:
            cur = cur + 1 if c in (a, b) else count_b + 1
            count_b = count_b + 1 if c == b else 1
            if b != c: a, b = b, c
            res = max(res, cur)
        return res
