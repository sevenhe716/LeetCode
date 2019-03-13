# Time:  O(n)
# Space: O(1)

# 解题思路：
# 动态规划
from functools import reduce


class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> int:
        cost1, cost2 = 0, 0
        for i in range(2, len(cost) + 1):
            cost1, cost2 = cost2, min(cost1 + cost[i-2], cost2 + cost[i-1])
        return cost2


class Solution1:
    def minCostClimbingStairs(self, cost):
        return min(reduce(lambda s, c: [c + min(s), s[0]], cost, [0]))

    def minCostClimbingStairs1(self, cost):
        s = [0]
        for c in cost:
            s = c + min(s), s[0]
        return min(s)