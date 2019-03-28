# Time:  O(logn!)
# Space: O(1)

# Ideas:
# binary search in two dimension, compare first and last in row and column
import bisect


class Solution:
    # O(lg(n!)) binary search reduction
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


class Solution1:
    #  O(lg(n!)) binary search
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if vertical:  # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:  # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True

        return False

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True

        return False

    # Divide and Conquer
    def searchMatrix1(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)

    # O(m+n) search space reduction
    def searchMatrix2(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False