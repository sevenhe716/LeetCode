# Time:  O(mn)
# Space: O(1)

# 解题思路：
# 与rotate_image思路类似，四个方向一圈圈往里遍历即可，注意每一行列都需要size-1
# 由于m, n可能不相等，最后需要特殊处理行或列遍历完的情况


class Solution:
    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        ans = []

        for i in range((min(m, n) + 1) >> 1):
            m_size = m - (i << 1)
            n_size = n - (i << 1)

            if m_size == 1:
                for j in range(n_size):
                    ans.append(matrix[i][i + j])
                break

            if n_size == 1:
                for j in range(m_size):
                    ans.append(matrix[i+j][i])
                break

            for j in range(n_size-1):
                ans.append(matrix[i][i + j])

            for j in range(m_size-1):
                ans.append(matrix[i + j][n - 1 - i])

            for j in range(n_size-1):
                ans.append(matrix[m - 1 - i][n - 1 - i - j])

            for j in range(m_size-1):
                ans.append(matrix[m - 1 - i - j][i])

        return ans

    # simulation
    def spiralOrder2(self, matrix: 'List[List[int]]') -> 'List[int]':
        if not matrix or not matrix[0]:
            return []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        bound_dirs = [(1, 0, 0, 0), (0, 0, 0, -1), (0, -1, 0, 0), (0, 0, 1, 0)]
        m, n = len(matrix), len(matrix[0])

        # start_r, end_r, start_c, end_c
        bound = [0, m - 1, 0, n - 1]
        res = []
        i, j = 0, -1
        while bound[0] <= bound[1] and bound[2] <= bound[3]:
            for dir, b_dir in zip(dirs, bound_dirs):
                i += dir[0]
                j += dir[1]
                while bound[0] <= i <= bound[1] and bound[2] <= j <= bound[3]:
                    res.append(matrix[i][j])
                    i += dir[0]
                    j += dir[1]
                # roll back
                i -= dir[0]
                j -= dir[1]

                bound[0] += b_dir[0]
                bound[1] += b_dir[1]
                bound[2] += b_dir[2]
                bound[3] += b_dir[3]

        return res

    # clean way
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        res = []
        r_start, r_end, c_start, c_end = 0, len(matrix), 0, len(matrix[0])
        while r_start < r_end and c_start < c_end:
            res += [matrix[r_start][j] for j in range(c_start, c_end)]
            r_start += 1
            res += [matrix[i][c_end-1] for i in range(r_start, r_end)]
            c_end -= 1
            if r_start < r_end:
                res += [matrix[r_end-1][j] for j in range(c_start, c_end)[::-1]]
                r_end -= 1
            if c_start < c_end:
                res += [matrix[i][c_start] for i in range(r_start, r_end)[::-1]]
                c_start += 1
        return res


class SolutionF:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result
        top = left = 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        while top < bottom and left < right:
            for i in range(left, right):
                result.append(matrix[top][i])
            for i in range(top, bottom):
                result.append(matrix[i][right])
            for i in range(right, left, -1):
                result.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                result.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            result.append(matrix[left][top])
        if left == right and top != bottom:
            for i in range(top, bottom+1):
                result.append(matrix[i][left])
        if left != right and top == bottom:
            for i in range(left, right+1):
                result.append(matrix[top][i])
        return result

    # one liner
    # |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
    # |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
    # |7 8 9|      |4 7|
    def spiralOrder1(self, matrix):
        # [*zip(*arr)]转置矩阵的方法，and返回右值
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])