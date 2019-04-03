# Time:  O(n)
# Space: O(1)

# 解题思路：
# 计数器，two-pass解法
# 进阶：使用one-pass且常数空间复杂度算法，可以尝试双指针交换
from collections import Counter


class Solution:
    def sortColors1(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)
        r, w, b = cnt.get(0, 0), cnt.get(1, 0), cnt.get(2, 0)
        nums[:r] = [0] * r
        nums[r:r+w] = [1] * cnt.get(1, 0)
        # 这里要注意，这种索引方式不能为0
        if b > 0:
            nums[-b:] = [2] * b

    # 三种元素交换，可以把两个元素看成一种，进行两次两元素加换
    # 也可以把一个元素和非此元素交换，再把一个元素跟非此元素加换
    # 常数时间，但依然是two-pass
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] == 0:
                left += 1
            while left < right and nums[right] != 0:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]

        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] != 2:
                left += 1
            while left < right and nums[right] == 2:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]

    # 尝试用四指针，两个遍历指针（->2， <-0），两个标记替换位置的指针(->!0, <-!2)
    # 貌似是一个吃力不讨好、事半功倍的解法, not finished
    def sortColors3(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        index_2, index_0 = 0, len(nums)-1
        index_not_0, index_not_2 = 0, len(nums)-1

        left, right = index_not_0, index_not_2
        print(nums)

        def find_left_bound():
            nonlocal left, index_not_0, index_not_2
            while left < index_not_2 and nums[left] == 0:
                left += 1
            if left < index_not_2:
                index_not_0 = left
                if nums[left] == 2:
                    # index_2 = left
                    if nums[index_not_2] != 0:
                        find_right_bound()
                    nums[left], nums[index_not_2] = nums[index_not_2], nums[left]
                    left += 1
                    index_not_2 -= 1
                else:
                    left += 1
                print('1: ', nums, left, right, index_not_0, index_not_2)

        def find_right_bound():
            nonlocal right, index_not_2, index_not_0
            while index_not_0 < right and nums[right] == 2:
                right -= 1
            print(right)
            if index_not_0 < right:
                index_not_2 = right
                if nums[right] == 0:
                    if nums[index_not_0] != 2:
                        find_left_bound()
                    nums[right], nums[index_not_0] = nums[index_not_0], nums[right]
                    right -= 1
                    index_not_0 += 1
                else:
                    right -= 1
                print('2: ', nums, left, right, index_not_0, index_not_2)

        while left < index_not_2 or index_not_0 < right:
            find_left_bound()
            find_right_bound()
            print(left, right, index_not_2, index_not_0)


class Solution1:
    # 1-pass 三指针法，容易理解
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
