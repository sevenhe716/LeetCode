# Time:  O(n)
# Space: O(n)

# 解题思路：
# BFS, DP, static DP and mathematics
from collections import deque


class Solution:
    # BFS, use list
    def numSquares1(self, n: int) -> int:
        nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        values1, values2, res = [0], [], 0
        visited = [False] * (n + 1)
        visited[0] = True

        while values1:
            res += 1
            for cur_value in values1:
                for num in nums:
                    new_value = cur_value + num
                    if new_value == n:
                        return res
                    # 后面的值更大，直接跳出
                    elif new_value > n:
                        break
                    else:
                        if not visited[new_value]:
                            visited[new_value] = True
                            values2.append(new_value)
            values1, values2 = values2, []
        # should never reach here

    # BFS, use set and deque，用如果队列则不是一轮一轮的传播，需要额外记录步长
    def numSquares2(self, n: int) -> int:
        nums = [i * i for i in range(1, int(n ** 0.5) + 1)]
        queue = deque([(0, 0)])
        visited = set()

        while queue:
            cur_value, step = queue.popleft()
            step += 1
            for num in nums:
                new_value = cur_value + num
                if new_value == n:
                    return step
                elif new_value > n:
                    break
                else:
                    if new_value not in visited:
                        visited.add(new_value)
                        queue.append((new_value, step))

    # DP，非常慢，因为每次都需要重复计算
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            dp[i] = min(dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)) + 1
        return dp[-1]


class Solution1:
    _dp = [0]

    # static DP
    def numSquares1(self, n):
        dp = self._dp
        while len(dp) <= n:
            # 加逗号，转化为tuple
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

    # math
    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """

        def is_square(n):
            if int(n ** 0.5) * int(n ** 0.5) == n:
                return True
            else:
                return False

        # n%4 == 0
        while (n % 4) == 0:
            n = int(n / 4)

        # 1 case
        if is_square(n):
            return 1
        # 4 case
        if n % 8 == 7:
            return 4
        # 2 case
        for i in range(1, int(n ** 0.5) + 1):
            if is_square(n - i * i):
                return 2
        else:
            return 3

    # bidirectional BFS
    # https://leetcode.com/problems/perfect-squares/discuss/188250/Python-bidirectional-BFS-(72ms-beats-90-faster-than-some-of-the-math-theorem-solutions)
    def numSquares(self, n):
        front, back, pm = [0], [n], 1 # pm is "plus minus"
        depth = [0] + [None] * (n - 1) + [-1] # depth[0] == 0, depth[n] == -1, depth[everythingElse] == None
        while front:
            newFront = []
            for v in front:
                i = 1
                while True:
                    w = v + pm * i * i # generate a neighbor
                    if w < 0 or w > n: # all neighbors have been generated
                        break
                    if depth[w] is None: # w has not been discovered
                        depth[w] = depth[v] + pm # mark it as discovered by assigning a depth to it
                        newFront.append(w)
                    elif (depth[w] < 0) != (depth[v] < 0): # w has been discovered in the `back` tree, so we're done
                        return abs(depth[w] - depth[v])
                    i += 1
            front = newFront
            if len(front) > len(back):
                front, back, pm = back, front, -pm # always expand the tree with fewer leaves

