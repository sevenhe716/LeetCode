# Time:  O(logn)
# Space: O(1)

# Ideas:
# binary search
# for [lo, mid], [mid, hi], find sorted interval and check this side
# mark


class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            # if nums[lo] == target:
            #     return lo
            # if nums[hi] == target:
            #     return hi
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1















        # print(nums)
        # lo, hi = 0, len(nums) - 1
        # while lo <= hi:
        #     mid = lo + (hi - lo) // 2
        #     print(nums[lo], nums[hi], nums[mid])
        #     if nums[mid] == target:
        #         return mid
        #     if nums[lo] == target:
        #         return lo
        #     if nums[hi] == target:
        #         return hi
        #     # if nums[lo] < nums[hi] and nums[mid] < target or nums[lo] > nums[hi] and nums[lo] > target:
        #     #     lo = mid + 1
        #     # else:
        #     #     hi = mid - 1
        #
        #     if nums[lo] < nums[hi]:
        #         if nums[mid] < target:
        #             lo = mid + 1
        #         else:
        #             hi = mid - 1
        #     else:
        #         if nums[mid] > target:
        #             if nums[lo] < nums[mid]:
        #                 hi = mid - 1
        #             else:
        #                 lo = mid + 1
        #         else:
        #             if nums[lo] < nums[mid]:
        #                 lo = mid + 1
        #             else:
        #                 hi = mid - 1
        #             # if target < nums[lo]:
        #             #     lo = mid + 1
        #             # else:
        #             #     hi = mid - 1
        #
        #         # if nums[mid] < target:
        #         #     if nums[hi] < nums[mid]:
        #         #         lo = mid + 1
        #         #
        #         #     if nums[hi] > target:
        #         #         lo = mid + 1
        #         #     else:
        #         #         hi = mid - 1
        #         # else:
        #         #
        #         #     if nums[lo] < target:
        #         #         hi = mid - 1
        #         #     else:
        #         #         lo = mid + 1
        # print(nums[hi])
        # return -1