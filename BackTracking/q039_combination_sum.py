# Time:  O(nlog(n))
# Space: O(1)

# 解题思路：
# 任意数量任意使用次数求和，考虑使用递归


# Recursion，也可以理解成BackTracking
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []

        def combinationSumR(left, target, cur_nums):
            if left >= len(candidates):
                return

            for i, num in enumerate(candidates[left:]):
                if target == num:
                    ans.append(cur_nums + [target])
                elif target > num:
                    combinationSumR(i + left, target - num, cur_nums + [num])
                else:  # 提前终止
                    return

        combinationSumR(0, target, [])

        return ans


# 其实用Stack来实现Recursion就是将Recursion需要的中间参数都压入栈中
# Stack Solution
class Solution1:
    def combinationSum(self, candidates, target):
        res, stack, n = [], [(0, [], 0)], len(candidates)  # Stack中塞入一组元素，值得借鉴
        while stack:
            sm, tmp, r = stack.pop()
            for i in range(r, n):
                if sm + candidates[i] < target:
                    stack.append((sm + candidates[i], tmp + [candidates[i]], i))      # 把所有可能需要的尝试都塞入Stack中，包括subsum，中间结果及左边界
                elif sm + candidates[i] == target:
                    res += [tmp + [candidates[i]]]
        return res


# BackTracking
class Solution2:
    def combinationSum(self, candidates, target):
        ans = []
        candidates.sort()

        def backtrack(tempList, remain, start):
            if remain < 0:
                return
            elif remain == 0:
                ans.append(list(tempList))
            else:
                for i in range(start, len(candidates)):
                    tempList.append(candidates[i])
                    backtrack(tempList, remain-candidates[i], i)
                    tempList.pop()
            pass

        backtrack([], target, 0)
        return ans
