# Time:  O(n)
# Space: O(1)

# Ideas:
# sort and BFS? but seems not fast
# optimization: cache while BFS
# mark


class Solution:
    def cutOffTree(self, forest: 'List[List[int]]') -> int:
        if not forest or not forest[0]:
            return 0
        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append(forest[i][j])
        trees.sort()
        start_state = (0, 0, 0)
        for tree in trees:
            queue = [start_state]
            visited = set()
            start_state = None
            for i, j, step in queue:
                visited.add((i, j))
                if forest[i][j] == tree:
                    start_state = (i, j, step)
                    break
                for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if 0 <= I < m and 0 <= J < n and forest[I][J] > 0 and (I, J) not in visited:
                        queue.append((I, J, step + 1))

            if not start_state:
                return -1

        return start_state[2]
