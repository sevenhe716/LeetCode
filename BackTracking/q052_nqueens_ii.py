# Time:  O(n!)
# Space: O(1)

# 解题思路：
# N皇后问题，回溯法，遍历行，维护列、左斜、右斜是否已占用
# 斜线的判断方法也可以用 abs(p1[0] - p2[0]) == abs(p1[1] - p2[1])


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = [False] * n
        left_cross = [False] * ((n << 1) - 1)
        right_cross = [False] * ((n << 1) - 1)
        count = 0

        def solve(x):
            nonlocal count
            if x == n:
                count = count + 1

            for y, c in enumerate(col):
                if not c and not left_cross[x + y] and not right_cross[n - x - 1 + y]:
                    col[y] = left_cross[x + y] = right_cross[n - x - 1 + y] = True
                    solve(x + 1)
                    col[y] = left_cross[x + y] = right_cross[n - x - 1 + y] = False

        solve(0)
        return count
