# Time:  O(n)
# Space: O(1)

# 解题思路：
# 从右往左找，直到一个不是逆序的元素为止，然后将首位与比它大的最小数交换，再将末尾插入排序到相应位置（降序），再整个反序
# 特殊情况：相等，已经是降序
# 优化：插入位置用二分查找，降序排列中的右插入


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        i = j = len(nums) - 1
        while i >= 1 and nums[i] <= nums[i - 1]:  # 是否有等于
            i -= 1

        i -= 1
        # i==0时直接反序
        if i >= 0:
            # 找到比首位大的最小数并交换，这里用降序的二分查找更快，插入到比它大的数的右侧
            lo, hi = i + 1, j + 1
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= nums[i]:
                    hi = mid
                else:
                    lo = mid + 1

            lo -= 1
            # while nums[j] <= nums[i]:
            #     j -= 1
            nums[i], nums[lo] = nums[lo], nums[i]

        i += 1
        # 再把末位插入升序的相应的位置
        # while i < j:
        #     if nums[j-1] < nums[j]:
        #         tmp = nums[j]
        #         nums[j], nums[j-1] = nums[j-1], tmp
        #         j -= 1
        #     else:
        #         break

        # nums[i, j+1]整体反序
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums
