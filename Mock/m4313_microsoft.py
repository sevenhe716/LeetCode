# Time:  O(n)
# Space: O(1)

# Ideas:
# binary search in two dimension, compare first and last in row and column
import bisect


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        start_r, end_r, start_c, end_c = 0, m - 1, 0, n - 1

        while start_r <= end_r and start_c <= end_c:
            # compare first in column
            row = matrix[start_r][start_c:end_c + 1]
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
            end_c = start_c + idx - 1

            # compare first in row
            col = [matrix[i][start_c] for i in range(start_r, end_r + 1)]
            idx = bisect.bisect_left(col, target)
            if idx < len(col) and col[idx] == target:
                return True
            end_r = start_r + idx - 1

            # compare last in column
            row = matrix[end_r][start_c:end_c + 1]
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
            start_c += idx

            # compare last in row
            col = [matrix[i][end_c] for i in range(start_r, end_r + 1)]
            idx = bisect.bisect_left(col, target)
            if idx < len(col) and col[idx] == target:
                return True
            start_r += idx

        return False
