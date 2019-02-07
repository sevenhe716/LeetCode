# Time:  O(n)
# Space: O(1)

# 解题思路：
# 不限制买卖次数，可以每天都先卖出再买入，如果当天是亏损的，那前一天就不买入了


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            # diff = prices[i+1] - prices[i]  # 临时变量的定义与回收成本比多一次计算更高
            # if diff > 0:
            #     profit = profit + diff
            if prices[i + 1] - prices[i] > 0:
                profit = profit + prices[i + 1] - prices[i]

        return profit
