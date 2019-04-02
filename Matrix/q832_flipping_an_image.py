# Time:  O(n)
# Space: O(1)

# 解题思路：
# 先水平翻转再取1的补数


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for row in A:
            row.reverse()
            for i, v in enumerate(row):
                row[i] = 1 - v

        return A


class SolutionF:
    def flipAndInvertImage(self, A):
        for row in A:
            for i in range((len(row) + 1) // 2):        # 长度要加1，保证遍历到中位数
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1       # 取反找到对称位置的写法借鉴，可以同时赋值无需临时变量
        return A
