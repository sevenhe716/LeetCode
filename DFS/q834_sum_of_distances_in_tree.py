# Time:  O(n)
# Space: O(1)

# 解题思路：
# 由于是全连通树（无环），从一个端点出发，用递归找到所有的path，将path沿途的所有线段加入到距离矩阵中，
# 再查找还剩余哪些点，换个端点继续执行


class Solution:
    def sumOfDistancesInTree1(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # dp
        dists = [[-1 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dists[i][i] = 0

        for edge in edges:
            dists[edge[0]][edge[1]] = dists[edge[1]][edge[0]] = 1

        while any(dists[i][j] < 0 for i in range(N) for j in range(N)):
            for dist_row in dists:
                for i in range(N - 1):
                    for j in range(N):
                        if dists[i][j] < 0 and dist_row[i] > 0 and dist_row[j] > 0:
                            dists[i][j] = dists[j][i] = dist_row[i] + dist_row[j]

        sums = [0] * N
        for i in range(N):
            for j in range(N):
                sums[i] += dists[i][j]

        return sums

    def sumOfDistancesInTree(self, N, edges):
        from functools import reduce

        if N == 1:
            return [0]

        dists = [[-1 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dists[i][i] = 0

        # convert to dict
        edge_dict = {}
        for edge in edges:
            edge_dict.setdefault(edge[0], []).append(edge[1])  # collections.defaultdict(list)
            edge_dict.setdefault(edge[1], []).append(edge[0])

            dists[edge[0]][edge[1]] = dists[edge[1]][edge[0]] = 1

        # end_point = -1
        #
        # # first find a end-point
        # for k, v in edge_dict.items():
        #     if len(v) == 1:
        #         end_point = k
        #         break

        # for i in range(N):
        #     count = reduce(lambda x, y: x + 1 if y[0] == i or y[1] == i else x, edges, 0)
        #
        #     if count == 1:
        #         break

        # print(edge_dict)
        # print(end_point)

        # self.sumOfDistancesInTreeR(edge_dict, [end_point], dists)

        in_progress = True
        while in_progress:
            in_progress = False
            is_find = False

            for i in range(N):
                if is_find:
                    break
                for j in range(N):
                    if dists[i][j] < 0:
                        in_progress = True
                        if len(edge_dict[i]) == 1:
                            self.sumOfDistancesInTreeR(edge_dict, [i], dists)
                            is_find = True
                            break
                        elif len(edge_dict[j]) == 1:
                            self.sumOfDistancesInTreeR(edge_dict, [j], dists)
                            is_find = True
                            break

        # if any(dists[i][j] < 0 for i in range(N) for j in range(N)):
        #     print('err')
        #     print(dists)
        #
        #     for i in range(N):
        #         for j in range(N):
        #             if dists[i][j] < 0:
        #                 print('i={}, j={}'.format(i, j))

        sums = [0] * N
        for i in range(N):
            for j in range(N):
                sums[i] += dists[i][j]

        return sums

    def sumOfDistancesInTreeR(self, edge_dict, path, dists):
        cur_node = path[-1]

        except_node = -1
        if len(path) > 1:
            except_node = path[-2]

        # print(path)

        for next_node in edge_dict[cur_node]:
            if next_node != except_node:
                path.append(next_node)

                for i, v in enumerate(path[:-2]):
                    if dists[v][next_node] < 0:
                        dists[v][next_node] = dists[next_node][v] = len(path) - i - 1

                self.sumOfDistancesInTreeR(edge_dict, path, dists)
                path.pop()


class Solution1(object):
    def sumOfDistancesInTree(self, N, edges):
        import collections

        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N

        def dfs(node=0, parent=None):
            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node)
                    count[node] += count[nei]
                    ans[node] += ans[nei] + count[nei]

        def dfs2(node=0, parent=None):
            for nei in graph[node]:
                if nei != parent:
                    ans[nei] = ans[node] - count[nei] + N - count[nei]
                    dfs2(nei, node)

        dfs()
        dfs2()
        return ans
