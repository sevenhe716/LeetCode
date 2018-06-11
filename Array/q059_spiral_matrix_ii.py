# Time:  O(n)
# Space: O(1)

# 解题思路：
# 跟spiral matrix思路类似，按照螺旋的顺序遍历即可
# 非常优雅的解法
# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        index = 0

        for i in range((n + 1) >> 1):
            n_size = n - (i << 1)

            if n_size == 1:
                index += 1
                matrix[i][i] = index
                break

            for j in range(n_size-1):
                index += 1
                matrix[i][i + j] = index

            for j in range(n_size-1):
                index += 1
                matrix[i + j][n - 1 - i] = index

            for j in range(n_size-1):
                index += 1
                matrix[n - 1 - i][n - 1 - i - j] = index

            for j in range(n_size-1):
                index += 1
                matrix[n - 1 - i - j][i] = index

        return matrix
