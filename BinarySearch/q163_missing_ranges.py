# Time:  O(n)
# Space: O(1)

# Ideas:
# binary search, two pointers, boundary included, special for one number
import bisect


class Solution:
    def findMissingRanges(self, nums: 'List[int]', lower: int, upper: int) -> 'List[str]':
        lo = bisect.bisect_left(nums, lower)
        hi = bisect.bisect_right(nums, upper)
        left = lower - 1
        res = []
        for num in nums[lo:hi+1] + [upper+1]:
            diff = num - left
            if diff == 2:
                res.append(str(num - 1))
            elif diff > 2:
                res.append(str(left + 1) + '->' + str(num-1))
            left = num

        return res
