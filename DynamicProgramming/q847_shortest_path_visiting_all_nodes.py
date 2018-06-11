# Time:  O(2^N∗N)
# Space: O(2^N∗N)

# 解题思路：
# 最优路径必定取决于连接数少的点，从连接数少的点开始逐步连通，直到全连接
# 找到一条最长尽可能覆盖多的路径，然后其他路径长度乘以2即可
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/


class Solution:
    # dp
    def shortestPathLength(self, graph):
        N = len(graph)
        dist = [[float('inf')] * N for i in range(1 << N)]
        for x in range(N):
            dist[1 << x][x] = 0

        for cover in range(1 << N):
            repeat = True
            while repeat:
                repeat = False
                for head, d in enumerate(dist[cover]):
                    for nei in graph[head]:
                        cover2 = cover | (1 << nei)
                        if d + 1 < dist[cover2][nei]:
                            dist[cover2][nei] = d + 1
                            if cover == cover2:
                                repeat = True

        return min(dist[2 ** N - 1])

    # BFS
    def shortestPathLength1(self, graph):
        import collections
        N = len(graph)
        queue = collections.deque((1 << x, x) for x in range(N))
        dist = collections.defaultdict(lambda: N * N)
        for x in range(N): dist[1 << x, x] = 0

        while queue:
            cover, head = queue.popleft()
            d = dist[cover, head]
            if cover == 2 ** N - 1: return d
            for child in graph[head]:
                cover2 = cover | (1 << child)
                if d + 1 < dist[cover2, child]:
                    dist[cover2, child] = d + 1
                    queue.append((cover2, child))
