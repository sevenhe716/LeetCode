# Time:  O(nlog(n))
# Space: O(n)

# 解题思路：
# 找到最高的点，往两侧找，不相邻的，两侧最大的元素，计算面积，利用分治法自顶向下分割，使用双指针直到移动到两端更佳
# 水的面积计算方式，由两个边界较小的那个决定面积再减去中间bar所占面积即可
# 优化思路：在寻找最大值时，每次都是重复的线性遍历，是否能将大小关系通过某种数据结构保存下来？只遍历一次生成这个数据结构即可
# 我想到的数据结构就是key为height的，value为索引的反向列表


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        height_sort = sorted([(v, i) for i, v in enumerate(height)])
        left_index = right_index = len(height_sort) - 1

        # def find_max(left, right):
        #     max_i, max_h = -1, 0
        #     for i in range(left, right):
        #         if height[i] > max_h:
        #             max_i, max_h = i, height[i]
        #     return max_i, max_h

        n = len(height)
        # mid, mid_h = find_max(0, n)
        # mid_h, mid = height_sort[height_sort]
        mid_h, mid = height_sort.pop()
        right_index -= 1
        left_index -= 1

        def find_max(left, right):
            left_max = right_max = -1

            while height_sort and (left_max != -1 or right_max != -1):
                h, index = height_sort.pop()
                if index < left:
                    left_max = index
                elif index >= right:
                    right_max = index

            return left_max, right_max

        left, right = mid, mid + 1
        trap = 0
        while left > 1 or right < n - 1:
            # mid_l, mid_r = find_max(left, right)
            # mid_l_h = height[mid_l]
            # mid_r_h = height[mid_r]

            if left > 1:
                # mid_l, mid_l_h = find_max(0, left - 1)
                mid_l, mid_l_h = -1, 0

                while left_index >= 0:
                    h, index = height_sort[left_index]
                    if index < left:
                        mid_l_h, mid_l = h, index
                        break

                    left_index -= 1

                if mid_l > -1:
                    trap += mid_l_h * (left - mid_l - 1)
                    # print('left l={} r={} area={} trap={}'.format(mid_l, left, mid_l_h * (left - mid_l - 1), trap))
                    for i in range(mid_l + 1, left):
                        trap -= height[i] if height[i] < mid_l_h else mid_l_h   # at most mid_l_h
                        # print('minus={} i={}'.format(height[i] if height[i] < mid_l_h else mid_l_h, i))

                    # print('trap2={}'.format(trap))
                left = mid_l

            if right < n - 1:
                mid_r, mid_r_h = n, 0

                while right_index >= 0:
                    h, index = height_sort[right_index]
                    if index > right:
                        mid_r_h, mid_r = h, index
                        break

                    right_index -= 1

                if mid_r < n:
                    # mid_r, mid_r_h = find_max(right + 1, n)
                    trap += mid_r_h * (mid_r - right)
                    # print('left l={} r={} area={} trap={}'.format(right-1, mid_r, mid_r_h * (mid_r - right), trap))
                    for i in range(right, mid_r):
                        trap -= height[i] if height[i] < mid_r_h else mid_r_h
                    # print('trap2={}'.format(trap))
                right = mid_r + 1

        return trap

        # def calc_trap(left, max_l, max_r, right):
        #     trap = 0
        #
        #     if left < max_l - 1:
        #         mid_l, mid_l_h = find_max(left, max_l - 1)
        #         trap += mid_l_h * (max_l - mid_l - 1)
        #         # calc trap
        #
        #     if max_r < right - 1:
        #         mid_r, mid_r_h = find_max(max_r + , right)
        #         trap += mid_r_h * (mid_r - max_r - 1)
        #
        #     return trap + calc_trap(left, mid_l, mid_r+1, right)
        #
        # mid, mid_h = find_max(0, len(height))
        # return calc_trap(0, mid_h, mid_h + 1, len(height))


# https://leetcode.com/problems/trapping-rain-water/solution/
# DP, Stack, TwoPointers

# Two-Pointers
class Solution1:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                tmp = height[left]
                left += 1
                while left < right and height[left] <= tmp:
                    result += tmp - height[left]
                    left += 1
            else:
                tmp = height[right]
                right -= 1
                while left < right and height[right] <= tmp:
                    result += tmp - height[right]
                    right -=1
        return result