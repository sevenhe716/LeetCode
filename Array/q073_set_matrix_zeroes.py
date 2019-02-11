# Time:  O(n)
# Space: O(1)

# 解题思路：
# 遍历记录所有应置0的行列，然后统一置0即可
# 优化思路，尝试矩阵运算加速？
# 进阶，常数空间复杂度的算法，比较tricky的一个想法是用位运算
# if i in rows or j in cols: 可以在一次循环中置0
# 正解是利用行列的头一个元素来存储为0的情况，这样降低了空间复杂度，同时统一赋值，时间复杂度也低

class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        zero_rows, zero_cols = 0, 0
        row_mask = 1
        for i, row in enumerate(matrix):
            col_mask = 1
            for j, v in enumerate(row):
                if v == 0:
                    zero_rows |= row_mask
                    zero_cols |= col_mask
                col_mask <<= 1
            row_mask <<= 1

        for i in range(m):
            if zero_rows == 0:
                break
            if zero_rows & 1 != 0:
                matrix[i] = [0] * n
            zero_rows >>= 1

        for j in range(n):
            if zero_cols == 0:
                break
            if zero_cols & 1 != 0:
                for i in range(m):
                    matrix[i][j] = 0
            zero_cols >>= 1


class Solution1:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0