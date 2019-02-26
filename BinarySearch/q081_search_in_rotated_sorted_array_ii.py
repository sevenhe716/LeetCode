# Time:  O(log(n)~n)
# Space: O(1)

# 解题思路：
# 旋转数组中查找元素，允许元素重复，二分查找


class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'bool':
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target or nums[lo] == target or nums[hi] == target:
                return True
            # 如果左右边界相等，则退化为线性查找，无法区分像113111111的情况
            if nums[lo] == nums[mid]:
                for i in range(lo+1, mid):
                    if nums[i] == target:
                        return True
                lo = mid + 1
            elif nums[mid] == nums[hi]:
                for i in range(mid+1, hi):
                    if nums[i] == target:
                        return True
                hi = mid - 1
            elif nums[lo] < nums[mid]:
                if nums[lo] < target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target < nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False
