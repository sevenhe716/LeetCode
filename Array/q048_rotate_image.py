# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 要求in-place 可以考虑一圈一圈的旋转，这样只用缓存一行
# 优化思路：其实可以在一个循环内完成，只要保证从最后一个元素开始交换就行

class Solution:
    def rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(n >> 1):
            size = n - (i << 1)
            tmp = matrix[i][i:i + size]

            for j in range(size):
                matrix[i][i + size - 1 - j] = matrix[i + j][i]

            for j in range(size):
                matrix[i + j][i] = matrix[n - 1 - i][i + j]

            for j in range(size):
                matrix[n - 1 - i][i + j] = matrix[i + size - 1 - j][n - 1 - i]

            for j in range(size):
                matrix[i + size - 1 - j][n - 1 - i] = tmp[size - 1 - j]


    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(n >> 1):
            size = n - (i << 1)

            for j in range(size-1):         # 这里注意用size-1，因为头尾在移动一次中同时完成
                tmp = matrix[i][i + size - 1 - j]
                matrix[i][i + size - 1 - j] = matrix[i + j][i]
                matrix[i + j][i] = matrix[n - 1 - i][i + j]
                matrix[n - 1 - i][i + j] = matrix[i + size - 1 - j][n - 1 - i]
                matrix[i + size - 1 - j][n - 1 - i] = tmp
