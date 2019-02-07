# Time:  O(n)
# Space: O(1)

# 解题思路：
# 比较常规的思路就是用dp, 状态定义：dp[i]表示第i天卖出的最大值，维护0-i的最小值，最终统计max(dp)即可
# 由于只需统计最大值，无需往回查找，则可以用一个变量存储即可

class Solution:
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 判断条件影响代码主干的执行效率
        if not prices:
            return 0
        lowest_buy, max_profit = prices[0], 0
        for i in range(len(prices)):
            # min max比if慢
            lowest_buy = min(prices[i], lowest_buy)
            max_profit = max(prices[i] - lowest_buy, max_profit)
        return max_profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_buy, max_profit = 2147483647, 0
        for price in prices:
            if price < lowest_buy:
                lowest_buy = price
            if max_profit < price - lowest_buy:
                max_profit = price - lowest_buy
        return max_profit
