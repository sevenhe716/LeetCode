# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if not matrix or not matrix[0]:
            return []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        bound_dirs = [(1, 0, 0, 0), (0, 0, 0, -1), (0, -1, 0, 0), (0, 0, 1, 0)]
        m, n = len(matrix), len(matrix[0])

        # start_r, end_r, start_c, end_c
        bound = [0, m-1, 0, n-1]
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
