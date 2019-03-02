# Time:  O(nlog(n))
# Space: O(1)

# 解题思路：
# O(n^2)的解法很容易想到，实际就是一个区间中的最小值乘以宽度，二维遍历即可
# 仔细分析可以发现，实际这是木桶原理，即由区间中最小高度所决定，因此可以按高度排序
# 再找到当前高度所处的区间范围，可以将时间复杂度降至O(nlog(n))
# 如何寻找当前位置的区间范围是算法的重点，线段树（区间树）能满足这个需求。
# 或者使用二分查找，时间复杂度nlog(n)
# Divide and Conquer：按最小高度来分割
# 线性时间复杂度的解法是使用栈，从左至右扫描
from bisect import bisect_left


class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        sorted_heights = sorted([(h, i) for i, h in enumerate(heights)])
        max_area, indexs = 0, []
        for h, i in sorted_heights:
            index = bisect_left(indexs, i)
            left = indexs[index - 1] if index - 1 >= 0 else -1
            right = indexs[index] if index < len(indexs) else len(heights)
            max_area = max(max_area, (right - left - 1) * h)
            indexs.insert(index, i)
        return max_area


class Solution1:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        s, res, heights = [], 0, [0] + heights + [0]
        for i, height in enumerate(heights):
            if len(s) > 0:
                while height < heights[s[-1]]:
                    top = s.pop()
                    res = max(res, heights[top] * (i - s[-1] - 1))
            s.append(i)
        return res
