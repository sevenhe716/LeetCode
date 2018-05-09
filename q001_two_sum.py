# Time:  O(n*log(n))
# Space: O(n)

# 解题思路：
# 有个显而易见的解法就是双循环遍历，但是时间复杂度是O(n^2)
# 首先我尝试排序数组，看是否能用二分查找，或由两端向中间搜索，或基于均值往两端遍历，可以把复杂度降到O(n*log(n))
# 但是不足之处在于，排序使得索引被破坏，需再进行O(n)的查找，且需要O(n)的额外空间
# 思考一下是否有O(n)复杂度的算法？


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort_nums = sorted(nums)            # 排序复杂度 O(n*log(n)), 额外空间复杂度O(n)
        start, end = 0, len(sort_nums) - 1  # if end < 1: return None #仅管题目提到have exactly one solution

        while True:
            s = sort_nums[start] + sort_nums[end]
            if s == target:    # 查找索引O(n)
                    s = nums.index(sort_nums[start])
                    e = len(nums) - nums[::-1].index(sort_nums[end]) - 1       # lastIndexOf，注意重复元素的问题
                    return [s, e]
            elif s < target:
                start += 1
            else:
                end -= 1

            if start >= end:
                return None     # 仅管题目提到have exactly one solution

    # 关键思路是把两数求和的问题，转化为遍历查找列表中剩余空间（或已索引空间）内的索引

    # Time:O(n)的解法
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i             # 创建一个lookup字典，保存索引及已经检查过的值

    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = 0
        for i in nums:
            j = target - i
            k += 1
            tmp_nums = nums[k:]
            if j in tmp_nums:
                return [k - 1, tmp_nums.index(j) + k]   # 利用切片来索引，无需额外空间，但是索引效率不如dict高


# map来索引已遍历数组里的差
class SolutionF:
    def twoSum(self, nums, target):
        complement = {}
        for i in range(len(nums)):
            if nums[i] in complement:
                return [complement[nums[i]], i]
            else:
                complement[target - nums[i]] = i

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


