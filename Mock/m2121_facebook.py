# Time:  O(n)
# Space: O(1)

# Ideas:
# dp


class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        if not prices:
            return 0
        lowest, max_profit = float('inf'), 0
        for p in prices:
            max_profit = max(max_profit, p - lowest)
            lowest = min(lowest, p)
        return max_profit