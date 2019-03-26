# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def nextPermutation(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        def reverse_inplace(i, j):
            left, right = i, j - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        for i in range(1, n)[::-1]:
            if nums[i - 1] < nums[i]:
                break
        else:
            reverse_inplace(0, n)
            return

        for j in range(i, n)[::-1]:
            if nums[j] > nums[i-1]:
                nums[j], nums[i-1] = nums[i-1], nums[j]
                break

        reverse_inplace(i, n)

