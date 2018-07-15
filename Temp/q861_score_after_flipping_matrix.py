# Time:  O(n)
# Space: O(1)

# 解题思路：
#

from common import print_matrix

# 不保证为1的优先不为0吗

class Solution:
    # greedy
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        m = len(A)
        n = len(A[0])

        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = 1 - A[i][j]

        for j in range(n):
            count = sum([A[i][j] for i in range(m)])
            if count < (m + 1) // 2:
                for i in range(m):
                    A[i][j] = 1 - A[i][j]

        print_matrix(A)
        ans = 0
        for i in range(m):
            cur = 0
            for j in range(n):
                cur <<= 1
                cur += A[i][j]

            ans += cur

        return ans