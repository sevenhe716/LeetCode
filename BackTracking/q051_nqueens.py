# Time:  O(n!)
# Space: O(1)

# 解题思路：
# N皇后问题，回溯法，遍历行，维护列、左斜、右斜是否已占用


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = [False] * n
        left_cross = [False] * ((n << 1) - 1)
        right_cross = [False] * ((n << 1) - 1)

        solution, ans = [['.'] * n for _ in range(n)], []

        def solve(x):
            if x == n:
                ans.append([''.join(x) for x in solution])

            for y, c in enumerate(col):
                if not c and not left_cross[x + y] and not right_cross[n - x - 1 + y]:
                    solution[x][y] = 'Q'
                    col[y] = left_cross[x + y] = right_cross[n - x - 1 + y] = True
                    solve(x + 1)
                    solution[x][y] = '.'
                    col[y] = left_cross[x + y] = right_cross[n - x - 1 + y] = False

        solve(0)
        return ans
