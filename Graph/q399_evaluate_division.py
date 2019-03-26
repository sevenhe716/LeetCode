# Time:  O(n)
# Space: O(1)

# Ideas:
# double direction graph, attention circle in graph and value is zero
# the implementation of graph is too heavy，directly use tuple list dict or dict dict
# UnionFind is also ok
import collections
import itertools


class Node:
    def __init__(self, name):
        self.name = name
        self.successors = []
        self.values = []


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, n1, n2, value):
        if n1 not in self.nodes:
            self.nodes[n1] = Node(n1)
        if n2 not in self.nodes:
            self.nodes[n2] = Node(n2)

        self.nodes[n1].successors.append(self.nodes[n2])
        self.nodes[n1].values.append(value)
        # consider divide zero situation
        if value != 0:
            self.nodes[n2].successors.append(self.nodes[n1])
            self.nodes[n2].values.append(1. / value)

    def calc(self, n1, n2):
        visited = set()
        queue = [(self.nodes[n1], 1.)]

        # BFS
        for node, res in queue:
            if node.name == n2:
                return res
            for successor, v in zip(node.successors, node.values):
                if successor not in visited:
                    visited.add(successor)
                    queue.append((successor, res * v))
        return -1


class Solution:
    def calcEquation(self, equations: 'List[List[str]]', values: 'List[float]',
                     queries: 'List[List[str]]') -> 'List[float]':
        graph = Graph()
        for eq, v in zip(equations, values):
            graph.add_edge(eq[0], eq[1], v)

        res = []
        for v1, v2 in queries:
            if v1 not in graph.nodes or v2 not in graph.nodes:
                res.append(-1.)
                continue
            res.append(graph.calc(v1, v2))

        return res


class Solution1:
    def calcEquation(self, equations, values, queries):
        quot = collections.defaultdict(dict)
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val
        # 计算所有路径
        for k, i, j in itertools.permutations(quot, 3):
            if k in quot[i] and j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]
        return [quot[num].get(den, -1.0) for num, den in queries]


class Solution2:
    def calcEquation(self, equations, values, queries):
        # 轻量级的有向图BFS解法
        graph = {}

        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]

            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1 / value)

        def find_path(query):
            b, e = query

            if b not in graph or e not in graph:
                return -1.0

            q = collections.deque([(b, 1.0)])
            visited = set()

            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product * value))

            return -1.0

        build_graph(equations, values)
        return [find_path(q) for q in queries]

# unoin find
class DJS:
    def __init__(self, alphabet):
        self.parent = {char: char for char in alphabet}
        self.vals = {char: 1.0 for char in alphabet}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x], val = self.find(self.parent[x])
            self.vals[x] *= val
        return self.parent[x], self.vals[x]

    def union(self, y, x, val):
        x, valx = self.find(x)
        y, valy = self.find(y)
        if x == y: return
        self.parent[y] = self.parent[x]
        self.vals[y] = val * valx / valy


class Solution3:
    def calcEquation(self, equations: 'List[List[str]]', values: 'List[float]',
                     queries: 'List[List[str]]') -> 'List[float]':
        alphabet = set(sum(equations, []))
        ufo = DJS(alphabet)
        for (y, x), val in zip(equations, values):
            ufo.union(y, x, val)

        res = []
        for y, x in queries:
            if x not in alphabet or y not in alphabet:
                res.append(-1.0)
                continue
            y, valy = ufo.find(y)
            x, valx = ufo.find(x)
            if x == y:
                res.append(valy / valx)
            else:
                res.append(-1.0)
        return res