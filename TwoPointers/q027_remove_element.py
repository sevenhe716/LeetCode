# Time:  O(n)
# Space: O(1)

# 解题思路：
# 算法要求原地删除，不需要考虑超出新长度后面的元素，且空间复杂度只能为O(1)
# 左右两个指针往中间移动，右指针移动直到不等于n，当左指针移动直到等于n，交换两数，直到两指针相遇
# 交换次数小于K，比较次数n
# 注意边界条件判断


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if not nums:
            return 0

        left, right = 0, len(nums) - 1
        count = len(nums)

        if left == right and nums[left] == val:
            return count - 1

        while left < right:
            while nums[right] == val and left < right:
                count -= 1
                right -= 1

            while nums[left] != val and left < right:
                left += 1

            if left == right:
                if nums[left] == val:
                    count -= 1
                return count

            count -= 1
            nums[left], nums[right] = nums[right], val
            left += 1
            right -= 1

        if left == right and nums[left] == val:
            count -= 1
        return count


# 相较于我的解法，只有左指针在移动，右指针只是在交换时移动，但是会出现如果num[last]=val，会交换两次
class Solution1:
    def removeElement(self, nums, val):
        i, last = 0, len(nums) - 1
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        return last + 1


# 破坏原数组的解法，赋值次数为n-k，当重复元素少时，不一定会最快
class SolutionF:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1
        return j
