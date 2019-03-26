# Time:  O(n)
# Space: O(1)

# Ideas:
# dp


class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        lowest, max_profit = float('inf'), 0
        for p in prices:
            if max_profit < p - lowest:
                max_profit = p - lowest
            if lowest > p:
                lowest = p
        return max_profit