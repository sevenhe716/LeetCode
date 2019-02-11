# Time:  O(n)
# Space: O(1)

# 解题思路：
# 满足上述性质的矩阵，平展开来事实上就是一个递增的有序数组
# 因此我们可以应用二分查找，只是把一维坐标映射到二维即可


class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            r, c = divmod(mid, n)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
