# Time:  O(n)
# Space: O(n)

# Ideas:
#


class Solution:
    def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        line_dict = {}

        for i in range(m):
            for j in range(n):
                if i - j not in line_dict:
                    line_dict[i - j] = matrix[i][j]
                elif line_dict[i - j] != matrix[i][j]:
                    return False
        return True
