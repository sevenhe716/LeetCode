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


# in python3, seems sort O(nlogn) is faster than stack or min_max O(n), maybe it is caused by lib.
class Solution1:
    # stack
    def findUnsortedSubarray(self, nums: 'List[int]') -> int:
        stack, n = [], len(nums)
        l, r = n, 0
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)

        stack.clear()

        for i in range(n)[::-1]:
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)

        return r - l + 1 if r - l > 0 else 0

    # without extra space
    def findUnsortedSubarray1(self, nums: 'List[int]') -> int:
        minimum, maximum = float('inf'), float('-inf')
        flag, n = False, len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                minimum = min(minimum, nums[i])

        flag = False
        for i in range(n - 1)[::-1]:
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                maximum = max(maximum, nums[i])

        for l in range(n):
            if minimum < nums[l]:
                break

        for r in range(n)[::-1]:
            if maximum > nums[r]:
                break

        return r - l + 1 if r - l > 0 else 0

    # faster by use lib
    def findUnsortedSubarray2(self, nums: 'List[int]') -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi and nums[lo] <= nums[lo + 1]:
            lo += 1
        if lo == len(nums) - 1:
            return 0
        while lo < hi and nums[hi] >= nums[hi - 1]:
            hi -= 1
        minVal = min(nums[lo:hi + 1])
        maxVal = max(nums[lo:hi + 1])
        while lo >= 0 and nums[lo] > minVal:
            lo -= 1
        while hi < len(nums) and nums[hi] < maxVal:
            hi += 1
        return hi - lo - 1
