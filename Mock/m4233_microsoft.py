# Time:  O(mnk)
# Space: O(mn)

# Ideas:
# trie + dfs
# trie tree to match all words in one visit


class Solution:
    def findWords(self, board: 'List[List[str]]', words: 'List[str]') -> 'List[str]':
        if not board or not board[0]:
            return []
        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]
        trie = {}
        for w in words:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            # record the whole words
            cur['#'] = w

        self.res = set()

        def dfs(i, j, trie):
            if '#' in trie:
                self.res.add(trie['#'])

            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n and not visited[I][J] and board[I][J] in trie:
                    visited[I][J] = 1
                    dfs(I, J, trie[board[I][J]])
                    visited[I][J] = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    visited[i][j] = 1
                    dfs(i, j, trie[board[i][j]])
                    visited[i][j] = 0

        return list(self.res)