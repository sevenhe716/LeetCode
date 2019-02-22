# Time:  O(n)
# Space: O(1)

# 解题思路：
# 常规思路是用回溯
# 优化：先通过计数器来作预检测
from collections import Counter


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        m, n = len(board), len(board[0])

        bcnts = Counter(c for r in board for c in r)

        for w, w_cnt in Counter(word).items():
            if w not in bcnts or w_cnt > bcnts[w]:
                return False

        def backtrack(i, j, index):
            if index == len(word) - 1:
                return True

            # 标记为已访问
            board[i][j] = '*'
            for dx, dy in dirs:
                next_i, next_j = i + dx, j + dy
                # 先判断再进入，减少递归次数
                if 0 <= next_i < m and 0 <= next_j < n and word[index + 1] == board[next_i][next_j] and backtrack(
                        next_i, next_j, index + 1):
                    return True

            board[i][j] = word[index]
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True

        return False
