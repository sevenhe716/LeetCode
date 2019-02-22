# Time:  O(n)
# Space: O(1)

# 解题思路：
#
import copy


class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        if nums:
            res = self.subsets(nums[:-1])
            res_copy = copy.deepcopy(res)
            for r in res:
                r.append(nums[-1])
            res += res_copy
            return res
        else:
            return [[]]

    def subsets1(self, nums: 'List[int]') -> 'List[List[int]]':
        res = [[]]

        def dfs(cur_nums):
            nonlocal res
            if cur_nums:
                res_copy = copy.deepcopy(res)
                for r in res:
                    r.append(cur_nums[0])
                res += res_copy
                dfs(cur_nums[1:])

        dfs(nums)
        return res


class Solution1:
    # iteratively
    def subsets1(self, nums: 'List[int]') -> 'List[List[int]]':
        res = [[]]
        for n in nums:
            # 边遍历边添加元素
            for i in range(len(res)):
                res.append(res[i] + [n])
        return res

    # one-line solution
    def subsets2(self, nums: 'List[int]') -> 'List[List[int]]':
        # 可以构造一个集合应用于for
        return [[], nums] if len(nums) == 1 else [i + j for i in self.subsets(nums[1:]) for j in [[], [nums[0]]]]

    # recursively
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums: return [[]]
        prefix = self.subsets(nums[:-1])
        return prefix + [pre + [nums[-1]] for pre in prefix]