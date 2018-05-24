# Time:  O(n)
# Space: O(1)

# 解题思路：
# 跟Combination Sum类似，区别在于数组中元素有重复，每个元素只能使用一次，同样使用回溯即可，先排序在遍历时可以提前终止
# 特殊情况：每个元素只能使用一次，但是可能有重复，结果中又不允许重复，所以需要去重
# 优化思路：for i in range(index, len(candidates)) 改为如果发现是重复的元素，则一直跳过至不同的元素为止


class Solution:
    # Backtracking by Stack
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        ans = set()
        stack = [(0, target, [])]  # index, remain, cur_nums

        while stack:
            index, remain, cur_nums = stack.pop()
            for i in range(index, len(candidates)):
                num = candidates[i]
                if num > remain:
                    break
                elif num == remain:
                    ans.add(tuple(cur_nums + [num]))        # list is mutable, unable to add to set, use tuple instead
                else:
                    stack.append((i + 1, remain - num, cur_nums + [num]))

        return [list(v) for v in ans]
