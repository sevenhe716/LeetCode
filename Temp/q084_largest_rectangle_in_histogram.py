# Time:  O(n)
# Space: O(1)

# 解题思路：
# O(n^2)的解法很容易想到，实际就是一个区间中的最小值乘以宽度，二维遍历即可
# 尝试使用动态规划来加速


class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        n = len(heights)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        min_height = heights[0]
        for i in range(n):
            min_height = min(min_height, heights[0])
            dp[0][i] = min_height * (i + 1)
        print(dp)
        return 0
