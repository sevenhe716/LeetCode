# Time:  O(n)
# Space: O(1)

# 解题思路：
# 动态规划维护二维数组，一维表示到第k天的最大利润，一维表示交易次数


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        lowest_price = 2147483647
        max_profit = 0
        dp = [[0 for _ in range(len(prices))] for _ in range(2)]
        for i in range(len(prices)):
            if lowest_price > prices[i]:
                lowest_price = prices[i]
            if max_profit < prices[i] - lowest_price:
                max_profit = prices[i] - lowest_price
            dp[0][i] = max_profit

        highest_price = 0
        for i in range(len(prices))[::-1]:
            if highest_price < prices[i]:
                highest_price = prices[i]
            dp[1][i] = dp[0][i] + (highest_price - prices[i] if highest_price - prices[i] > 0 else 0)

        return max(dp[1])

