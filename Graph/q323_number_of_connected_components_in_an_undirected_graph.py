# Time:  O(n)
# Space: O(1)

# 解题思路：
# 并查集，对于稀疏矩阵，也可以用DFS，BFS
from functools import reduce


class Solution:
    def countComponents(self, n: int, edges: 'List[List[int]]') -> int:
        roots = [i for i in range(n)]

        def find(x):
            root = x
            while root != roots[root]:
                root = roots[root]
            # 路径压缩
            while x != roots[x]:
                x, roots[x] = roots[x], root
            return root

        def union(x, y):
            roots[find(x)] = find(y)

        for x, y in edges:
            union(x, y)

        return len(set([find(x) for x in roots]))


class Solution1:
    # pythonic one-line，先把int映射为unicode char，然后再replace进行合并，这里用到了reduce实现批量replace，unicode的妙用
    def countComponents1(self, n, edges):
        return len(set(reduce(lambda c, edge: c.replace(c[edge[1]], c[edge[0]]), edges, ''.join(map(chr, range(n))))))

    # dfs
    def countComponents2(self, n, edges):
        def dfs(n, g, visited):
            if visited[n]:
                return
            visited[n] = 1
            for x in g[n]:
                dfs(x, g, visited)

        visited = [0] * n
        g = {x: [] for x in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ret = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, g, visited)
                ret += 1

        return ret

    # bfs
    def countComponents3(self, n, edges):
        g = {x: [] for x in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ret = 0
        for i in range(n):
            queue = [i]
            ret += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return ret