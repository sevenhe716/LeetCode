# Time:  O(n)
# Space: O(1)

# 解题思路：
# 递归
from functools import reduce


class Solution:
    def combine1(self, n: 'int', k: 'int') -> 'List[List[int]]':
        res = []

        def combineR(cur, i):
            if len(cur) == k:
                res.append(cur)
                return
            if i > n:
                return
            combineR(cur + [i], i + 1)
            combineR(cur, i + 1)

        combineR([], 1)
        return res

    # 自递归
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        if k == 0:
            return [[]]
        # 不包含或者包含第n个元素
        return self.combine(n - 1, k) + [l + [n] for l in self.combine(n - 1, k - 1)] if n >= 1 else []


class Solution1:
    # recusively
    def combine1(self, n: 'int', k: 'int') -> 'List[List[int]]':
        if k == 0:
            return [[]]
        # 递归前缀，每次添加最后一个元素
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]

    # iteratively
    def combine2(self, n: 'int', k: 'int') -> 'List[List[int]]':
        res = [[]]
        for _ in range(k):
            # 从大到小，每次添加最后一个元素，最后一个元素的取值范围为:[1,前一个元素)
            res = [[i] + c for c in res for i in range(1, c[0] if c else n+1)]
        return res

    # reduce
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        res = [[]]
        for _ in range(k):
            res = reduce(lambda x, y: x + [[i] + y for i in range(1, y[0] if y else n+1)], res, [])
        return res
