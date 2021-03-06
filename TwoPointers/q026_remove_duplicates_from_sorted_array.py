# Time:  O(n)
# Space: O(1)

# 解题思路：
# 算法要求原地删除，不需要考虑超出新长度后面的元素，且空间复杂度只能为O(1)
# 算法可以分为三步：
# 1. 左右两个指针，把大的元素往左边替换，直到左右两个指针相遇
# 2. 然后再从相遇点往右找所有小于相遇值的元素并换到左侧
# 3. 最后将左指针左侧的数组反序即可
# 时间复杂度分析：若不重复的元素个数为K，交换次数为k+k/2+1
# 优化思路：双指针遍历：一个slow-runner 一个fast-runner，破坏原数组，检测到重复的元素直接赋值覆盖


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        left, right = 0, len(nums)-1

        if nums[left] == nums[right]:
            return 1

        cur_num = 2147483647

        while left < right:
            if nums[left] == nums[right]:
                break

            while nums[right] >= cur_num and left < right:
                right -= 1

            if left >= right:
                break

            cur_num = nums[right]
            nums[right], nums[left] = nums[left], cur_num     # swap
            # cur_num, nums[right], nums[left] = nums[left], cur_num, nums[right]     # 错误写法，因为并行是同时赋值
            left += 1
            right -= 1

        mid = left
        cur_num = nums[mid - 1]
        for i in range(mid, len(nums)):
            if nums[i] < cur_num:
                cur_num = nums[i]
                nums[i], nums[left] = nums[left], cur_num
                left += 1

        mid = left
        right, left = left-1, 0
        while left < right:
            cur_num = nums[right]
            nums[right], nums[left] = nums[left], cur_num
            left += 1
            right -= 1
        return mid


# 直接比较最后一个元素是否与当前元素相等即可，因为后面的数一定大于等于最后一个数，如果不等那就是满足条件的数
# 破坏原数组的解法
class SolutionF:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        last, i = 0, 1
        while i < len(nums):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i]
            i += 1

        return last + 1
