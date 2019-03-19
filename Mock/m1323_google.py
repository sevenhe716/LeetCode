# Time:  O(n)
# Space: O(1)

# Ideas:
# double direction graph, attention circle in graph and value is zero

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
        if value != 0:
            self.nodes[n2].successors.append(self.nodes[n1])
            self.nodes[n2].values.append(1. / value)

    def calc(self, n1, n2):
        visited = set()
        queue = [(self.nodes[n1], 1.)]

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
        variables, graph = set(), Graph()
        for eq, v in zip(equations, values):
            variables.add(eq[0])
            variables.add(eq[1])
            graph.add_edge(eq[0], eq[1], v)

        res = []
        for v1, v2 in queries:
            if v1 not in variables or v2 not in variables:
                res.append(-1.)
                continue
            if v1 == v2:
                res.append(1.)
                continue
            res.append(graph.calc(v1, v2))

        return res
