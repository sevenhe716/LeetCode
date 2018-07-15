# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        m, n = len(A), len(A[0])

        AT = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                AT[j][i] = A[i][j]

        return AT