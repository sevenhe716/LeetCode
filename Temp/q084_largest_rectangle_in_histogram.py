# Time:  O(nlog(n))
# Space: O(1)

# 解题思路：
# O(n^2)的解法很容易想到，实际就是一个区间中的最小值乘以宽度，二维遍历即可
# 仔细分析可以发现，实际这是木桶原理，即由区间中最小高度所决定，因此可以按高度排序
# 再找到当前高度所处的区间范围，可以将时间复杂度降至O(nlog(n))
# 如何寻找当前位置的区间范围是算法的重点，可以尝试使用二叉排序树，按前序遍历，其相邻的两个节点即是区间范围
# 二叉平衡树，一方面工作是插入，维护此数据结构，同时需要寻找到左右相邻的节点

class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        left, right = 0, len(heights) - 1

        sorted_heights = []
        for i, h in enumerate(heights):
            sorted_heights.append((h, i))

        sorted_heights.sort()

        max_area = 0

        for h, i in sorted_heights:
            max_area = max(max_area, (right - left + 1) * h)


