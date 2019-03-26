# Time:  O(n)
# Space: O(1)

# 解题思路：
# 多个匹配需要同时消除


class Solution:
    def candyCrush(self, board: 'List[List[int]]') -> 'List[List[int]]':
        m, n = len(board), len(board[0])

        def scan():
            mask = set()
            for i in range(m):
                char, cnt = 0, 1
                for j in range(n):
                    if char != board[i][j]:
                        if cnt >= 3 and char != 0:
                            mask |= {(i, k) for k in range(j - cnt, j)}
                        char, cnt = board[i][j], 1
                    else:
                        cnt += 1
                if cnt >= 3 and char != 0:
                    mask |= {(i, k) for k in range(n - cnt, n)}

            for j in range(n):
                char, cnt = 0, 1
                for i in range(m):
                    if char != board[i][j]:
                        if cnt >= 3 and char != 0:
                            mask |= {(k, j) for k in range(i - cnt, i)}
                        char, cnt = board[i][j], 1
                    else:
                        cnt += 1
                if cnt >= 3 and char != 0:
                    mask |= {(k, j) for k in range(m - cnt, m)}
            return mask

        # crush
        def crush():
            for j in range(n):
                offset = 0
                for i in range(m)[::-1]:
                    if offset > 0:
                        board[i + offset][j] = board[i][j]
                    if (i, j) in mask:
                        offset += 1
                for k in range(offset):
                    board[k][j] = 0

        mask = scan()
        while mask:
            crush()
            mask = scan()
        return board

# Rotate the board will make the drop operation much easier. That being said, instead of move all non-zero value to the
#  end of each column, the drop operation becomes move all non-zero value to the beginning of each row.
class Solution1:
    def candyCrush(self, board):
        board = map(list, zip(*reversed(board)))  # rotate clockwise 90 degree
        m, n = len(board), len(board[0])

        # repeat crush and drop
        while True:
            candy = set([])
            # check every row
            for i in range(m):
                for j in range(2, n):
                    if board[i][j] and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        candy |= {(i, j), (i, j - 1), (i, j - 2)}
            # check every col
            for j in range(n):
                for i in range(2, m):
                    if board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        candy |= {(i, j), (i - 1, j), (i - 2, j)}
            if not candy: break
            for i, j in candy: board[i][j] = 0

            # drop the board, move non-zero to the beginning of each row.
            for i in range(m):
                row = filter(None, board[i])
                board[i] = row + [0] * (n - len(row))

        board = list(reversed(map(list, zip(*board))))  # rotate counter-clockwise 90 degree
        return board