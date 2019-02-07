# Time:  O(n)
# Space: O(1)

# 解题思路：
# 1. 数组拼接
# 2. 缓存需要旋转的数据
# 3. 数组翻转再分别翻转
# 4. 要求O(1) extra space的解法，冒泡k次？


class Solution:
    # 三次翻转，O(1)空间复杂度
    def rotate(self, nums: 'List[int]', k: 'int',) -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)


    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n



