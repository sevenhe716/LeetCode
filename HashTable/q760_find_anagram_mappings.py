# Time:  O(n)
# Space: O(n)

# 解题思路：
# AB中的元素允许重复，可以考虑在B上建索引，注意因为元素可以重复，value是索引的列表
# 题目的意思不需要返回唯一的索引
from collections import defaultdict


class Solution:
    def anagramMappings1(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        b_idx = defaultdict(list)
        for i, b in enumerate(B):
            b_idx[b].append(i)

        # 输入保证B一定是A的anagram
        # 一次性初始化后赋值是否比append效率高？

        res = [0] * len(A)
        for i, a in enumerate(A):
            res[i] = b_idx[a].pop()

        # res = []
        # for a in A:
        #     res += [b_idx[a].pop()]
        return res

    def anagramMappings2(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        b_idx = defaultdict(list)
        for i, b in enumerate(B):
            b_idx[b].append(i)
        return list(map(lambda x: b_idx[x].pop(), A))

    def anagramMappings(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        b_idx = {b: i for i, b in enumerate(B)}
        return [b_idx[a] for a in A]
