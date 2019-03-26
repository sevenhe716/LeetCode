# Time:  O(mn)
# Space: O(m+n)

# Ideas:
#


class Solution:
    def isToeplitzMatrix(self, matrix: 'List[List[int]]') -> bool:
        line_dict = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - j not in line_dict:
                    line_dict[i - j] = matrix[i][j]
                elif line_dict[i - j] != matrix[i][j]:
                    return False
        return True


# 这也是一种不错的思路，无需推导复杂的索引规则，直接整体遍历并判断与左上的元素即可
class Solution1:
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))
