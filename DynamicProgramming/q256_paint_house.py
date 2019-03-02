# Time:  O(n)
# Space: O(1)

# 解题思路：
# 只需要相邻的两个房子用不同的颜色，因此我们可以用动态规划记录当前选择这个颜色的最小开销即可


class Solution:
    def minCost(self, costs: 'List[List[int]]') -> int:
        min_cost = [0] * 3
        for cost in costs:
            min_cost[0], min_cost[1], min_cost[2] = cost[0] + min(min_cost[1], min_cost[2]), \
                    cost[1] + min(min_cost[0], min_cost[2]), cost[2] + min(min_cost[0], min_cost[1])
        return min(min_cost)
