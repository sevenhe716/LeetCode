# Time:  O(n)
# Space: O(1)

# 解题思路：
# 旋转数组中查找，二分查找，若nums[lo]>nums[hi] x>nums[lo]，则在左半，若x<nums[hi]，则在右半，若nums[hi]<x<nums[lo]则不存在


class Solution1:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            # print('{}-{}-{}', lo, hi, nums[lo:hi])
            if target == nums[lo]:
                return lo
            if target == nums[hi - 1]:
                return hi - 1

            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid

            if nums[lo] > nums[hi - 1]:
                if target < nums[hi - 1]:
                    if target < nums[mid] < nums[hi - 1]:
                        hi = mid
                    else:
                        lo = mid + 1

                    # if nums[mid] > nums[hi - 1]:
                    #     lo = mid + 1
                    # else:
                    #     if target < nums[mid]:
                    #         hi = mid
                    #     else:
                    #         lo = mid + 1
                elif target > nums[lo]:
                    if target > nums[mid] > nums[lo]:
                        lo = mid + 1
                    else:
                        hi = mid

                    # if nums[mid] < nums[lo]:
                    #     hi = mid
                    # else:
                    #     if target < nums[mid]:
                    #         hi = mid
                    #     else:
                    #         lo = mid + 1
                else:
                    return -1
            else:  # 已经变为升序
                if target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1

        return -1


# Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# Because it's not fully sorted, we can't do normal binary search. But here comes the trick:
#
# If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
# [12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
#
# If target is let's say 7, then we adjust nums to this:
# [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# And then we can simply do ordinary binary search.
#
# Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements we look at.
#  And the adjustment is done by comparing both the target and the actual element against nums[0].

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MIN_INT32 = -2147483648
        MAX_INT32 = 2147483647

        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2

            # 比较运算符优先级高于等于运算符？？经测试是同一优先级
            num = nums[mid] if (nums[mid] < nums[0]) == (target < nums[0]) else MIN_INT32 if target < nums[0] else MAX_INT32

            if target > num:
                lo = mid + 1
            elif target < num:
                hi = mid
            else:
                return mid

        return -1

