# Time:  O(mn)
# Space: O(1)

# 解题思路：
# 与rotate_image思路类似，四个方向一圈圈往里遍历即可，注意每一行列都需要size-1
# 由于m, n可能不相等，最后需要特殊处理行或列遍历完的情况


class Solution:
    def spiralOrder(self, matrix):
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