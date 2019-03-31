# Time:  O(n)
# Space: O(1)

# 解题思路：
# 两种思路：可以用计数器为单位来做迭代，或者是先排序，递归时区分相同元素，避免重复添加
from collections import Counter


class Solution:
    # iteratively
    def subsetsWithDup1(self, nums: 'List[int]') -> 'List[List[int]]':
        cnt = Counter(nums)
        paths = [[]]
        for k, v in cnt.items():
            new_paths = []
            for i in range(v + 1):
                new_paths += [path + [k] * i for path in paths]
            paths = new_paths
        return paths

    # recursively, dfs
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []
        nums.sort()

        def dfs(start, path):
            # 抛弃后续元素
            res.append(path)
            for i in range(start, len(nums)):
                # 重复元素只添加第一个，后续元素直接跳过，避免重复（相当于相同元素有内部序号）
                if i > start and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path + [nums[i]])

        dfs(0, [])
        return res
