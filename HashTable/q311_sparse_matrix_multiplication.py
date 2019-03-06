# Time:  O(n)
# Space: O(1)

# 解题思路：
# 考虑压缩矩阵，左矩阵按行压缩，右矩阵按列压缩


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(B[0])
        a_rows = []
        for rows in A:
            a_rows.append({col: v for col, v in enumerate(rows) if v != 0})

        b_cols = []
        for j in range(n):
            b_cols.append({i: B[i][j] for i in range(len(B)) if B[i][j] != 0})

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k, v in a_rows[i].items():
                    if k in b_cols[j]:
                        res[i][j] += v * b_cols[j][k]
        return res
