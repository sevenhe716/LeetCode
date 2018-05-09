# Time:  O(n)
# Space: O(1)

# 解题思路：
# 该问题可以转化为从两端往中间找x, y，使得min(a(x), a(y))*(y-x)最大
# 观察规律：比较a(x), a(y)，从较小的那侧去寻找第一个大于它的元素，再按照这个规律找下去，就能找到所有满足条件的候选对
# 若边界相等的话，可以随意找哪边，并不影响结果，因为下一次将会找另外一边


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left, right = 0, len(height)-1
        area_max = (right - left) * min(height[left], height[right])

        while left < right:
            if height[left] <= height[right]:               # 判断左右边界哪个起到面积决定性作用
                index = left + 1
                while height[index] <= height[left]:        # 找到第一个比左边界大的元素
                    index += 1
                    if index >= right:
                        return area_max
                left = index
                area_max = max(area_max, (right - left) * min(height[left], height[right]))
            else:
                index = right - 1
                while height[index] <= height[right]:        # 找到第一个比右边界小的元素
                    index -= 1
                    if index <= left:
                        return area_max
                right = index
                area_max = max(area_max, (right - left) * min(height[left], height[right]))

        return area_max


# 不单独讨论找比边界小的元素，而是直接统一通过面积来比较
class Solution1:
    # @return an integer
    def maxArea(self, height):
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


class SolutionF:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        left = 0
        right = len(height) - 1
        max = 0
        while left < right:
            if height[left] >= height[right]:
                tempMax = (right - left) * height[right]
                right -= 1
            else:
                tempMax = (right - left) * height[left]
                left += 1
            if tempMax > max:
                max = tempMax

        return max


# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
