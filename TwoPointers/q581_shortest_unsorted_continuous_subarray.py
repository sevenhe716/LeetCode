# Time:  O(nlog(n))
# Space: O(n)

# 解题思路：
# nlog(n)的解法很容易想到，排序后去除首尾匹配的部分


class Solution:
    def findUnsortedSubarray(self, nums: 'List[int]') -> int:
        sort_nums = sorted(list(nums))
        n = len(sort_nums)
        for i in range(n):
            if nums[i] != sort_nums[i]:
                start = i
                break
        else:
            return 0

        for i in range(n)[::-1]:
            if nums[i] != sort_nums[i]:
                end = i
                break
        else:
            return 0

        return end - start + 1
