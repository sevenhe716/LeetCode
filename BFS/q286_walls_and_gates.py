# Time:  O(mn)
# Space: O(mn)

# 解题思路：
# 一个比较直观的思路是BFS，当遇到门或者障碍，或者更短距离时，终止循环。
# 优化：每个空房间只需要遍历一次，由于是多个门同时BFS，空房间被赋值时一定是最短路径
# DFS比BFS慢，因为BFS每个节点只用访问一次，而DFS要一直访问到最短路径

class Solution:
    # 优化：step可以直接从rooms里面读，dirs可以构造到for里
    def wallsAndGates1(self, rooms: 'List[List[int]]') -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        bfs = [(i, j, 0) for i in range(m) for j in range(n) if rooms[i][j] == 0]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j, step in bfs:
            step += 1
            for dir in dirs:
                cur_i = i + dir[0]
                cur_j = j + dir[1]
                if 0 <= cur_i < m and 0 <= cur_j < n and rooms[cur_i][cur_j] > step:
                    rooms[cur_i][cur_j] = step
                    bfs.append((cur_i, cur_j, step))

    def wallsAndGates(self, rooms: 'List[List[int]]') -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        bfs = [(i, j) for i, row in enumerate(rooms) for j, v in enumerate(row) if not v]
        for i, j in bfs:
            for I, J in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2 ** 30:
                    rooms[I][J] = rooms[i][j] + 1
                    bfs += (I, J),


class Solution1:
    # dfs，比BFS慢，因为BFS每个节点只用访问一次，而DFS要一直访问到最短路径
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        def dfs(i, j, m, n, dist):
            if 0 <= i <= m - 1 and 0 <= j <= n - 1 and rooms[i][j] >= dist:
                rooms[i][j] = dist
                for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    dfs(r, c, m, n, dist + 1)

        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i, j, m, n, 0)