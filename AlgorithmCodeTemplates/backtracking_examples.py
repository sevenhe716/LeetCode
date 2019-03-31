# [51] https://leetcode.com/problems/n-queens/
# Given an integer n, return all distinct solutions to the n-queens puzzle.
def solveNQueens(n):
    result = []

    def backtracking(queens, xy_diff, xy_sums):
        p = len(queens)
        if p == n:
            result.append(queens)
            return
        for q in range(n):
            if q not in queens and p - q not in xy_diff and p + q not in xy_sums:
                backtracking(queens + [q], xy_diff | {p - q}, xy_sums | {p + q})

    backtracking([], set(), set())
    return [['.' * i + 'Q' + '.' * (n - i - 1) for i in queen] for queen in result]


# [37] https://leetcode.com/problems/sudoku-solver/
# easy-understanding version, not a efficient solution
# optimize: use priority queue and bit-manipulation
def solveSudoku(board):
    stack = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]

    def dfs():
        if not stack:
            return
        x, y = stack.pop()
        box = [board[x // 3 * 3 + i][y // 3 * 3 + j] for i in range(3) for j in range(3)]
        row = [board[x][j] for j in range(9)]
        col = [board[i][y] for i in range(9)]
        for i in "123456789":
            if not any([i in box, i in col, i in row]):
                board[x][y] = i
                dfs()
                if not stack:
                    return
        board[x][y] = "."
        stack.append((x, y))

    dfs()
