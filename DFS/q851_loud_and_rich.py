# Time:  O(n)
# Space: O(n)

# 解题思路：
# 找到最大的值，即左值不在任意一个右值中，按此方式缓存左值到列表的字典，以及右值的计数器，按最大值的方式迭代删除，直到集合为空即可


class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        import collections

        n = len(quiet)
        # ans = [-1] * n

        ans = [i for i in range(n)]

        richer2 = {}
        for x in richer:
            if x[0] not in richer2:
                richer2[x[0]] = [x]
            else:
                richer2[x[0]].append(x)

        counter = collections.Counter([x[1] for x in richer])

        while richer2:
            for x in richer2:
                if x not in counter:
                    for y in richer2[x]:
                        counter[y[1]] -= 1
                        if counter[y[1]] == 0:
                            counter.pop(y[1])

                        if quiet[ans[y[0]]] < quiet[ans[y[1]]]:
                            ans[y[1]] = ans[y[0]]

                    richer2.pop(x)
                    break

        return ans


# 反向索引图，Now dfs(person) is either person, or min(dfs(child) for child in person)
# dfs中作缓存，则会去掉重复工作，让时间复杂度降为线性
class Solution1(object):
    def loudAndRich(self, richer, quiet):
        N = len(quiet)
        graph = [[] for _ in range(N)]
        for u, v in richer:
            graph[v].append(u)

        answer = [None] * N
        def dfs(node):
            #Want least quiet person in this subtree
            if answer[node] is None:
                answer[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[answer[node]]:
                        answer[node] = cand
            return answer[node]

        return map(dfs, range(N))

    # 思路类似，另一种写法
    def loudAndRich1(self, richer, quiet):
        import collections
        edges, memo, res = collections.defaultdict(list), {}, [i for i in range(len(quiet))]
        for r, p in richer: edges[p].append(r)

        def explore(i):
            if i in memo: return memo[i]
            cur_min = i
            for v in edges[i]:
                cur = explore(v)
                if quiet[cur] < quiet[cur_min]: cur_min = cur
            res[i] = memo[i] = cur_min
            return cur_min

        for i in range(len(quiet)): explore(i)
        return res
