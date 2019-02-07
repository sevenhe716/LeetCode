# Time:  O(n)
# Space: O(1)

# 解题思路：
# 状态可以表示为当天卖出的最大收益（也需要一直遍历统计出最小值），或者是统计到这一天的最大收益
# 存在的问题是，对于买入和卖出的时间只能记录其中一个，另一个需要在运行时计算，如统计当前的最低价
# 优化思路：再增加一个维度，记录买入或卖出的状态
#
# 这里存在一个问题，买入一股肯定比什么都不做要暂时损失一部分利益，
# 感觉通过这个指标来决定状态是不妥当的，保持不动肯定比买入的眼前利益是更高的，卖出也是同理
# 其实不然，对于当前状态的局部最优解（当前的那一天、当前交易次数、当前拥有股票数）相当于运用了局部的贪心算法
#
# 另一个优化思路：当交易次数K大于天数时，可以退化成无交易次数上限的算法，即普通贪心即可

import common

class Solution:
    def maxProfit1(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        dp = [0] * n

        # 缓存min_val, 可以减少k-1次min_price计算，但是空间复杂度较大
        min_vals = [[0] * n for _ in range(n)]
        for i in range(n-1):
            min_price = 2147483647
            for j in range(i, n):
                if min_price > prices[j]:
                    min_price = prices[j]
                min_vals[i][j] = min_price

        for i in range(k):
            dp2 = [0] * n
            for j in range(n):
                for x in range(j)[::-1]:
                    if prices[j] - min_vals[x][j] > 0:
                        dp2[j] = max(dp2[j], dp[x] + prices[j] - min_vals[x][j])
            dp = dp2
        return max(dp)


    def maxProfit2(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        dp = [0] * n

        # 依然超时，再减少一层循环
        for i in range(k):
            dp2 = [0] * n
            max_profit = 0
            min_price = 27483647
            for j in range(n):
                # 统计当前的最小值，需要有个区间，相减即可
                if min_price > prices[j]:
                    min_price = prices[j]

                dp2[j] = max(dp2[j], prices[j] - min_price + dp[x])

                for x in range(j)[::-1]:
                    dp2[j] = max(dp2[j], dp[x] + prices[j] - prices[x], max_profit)
                    if max_profit < dp2[j]:
                        max_profit = dp2[j]
                    # if prices[j] - min_vals[x][j] > 0:
                    #     dp2[j] = max(dp2[j], dp[x] + prices[j] - min_vals[x][j])
            dp = dp2
        return dp[n-1]

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        # 状态定义：至今的最大收益, 0: 当前拥有0股，可买入，1：当前拥有1股，可卖出
        # mp = [[[0 for _ in range(n)] for _ in range(2)] for _ in range(k+1)]
        # 边界条件：初始化第一次交易前的状态，每次交易的第一天

        # n天的交易次数最多可以n-1次，当大于等于这个数时，可以视为无限次交易，直接用贪心算法，减少dp的次数
        if k >= n-1:
            max_profit = 0
            for i in range(n-1):
                max_profit = max_profit + (prices[i+1] - prices[i] if prices[i+1] - prices[i] > 0 else 0)
            return max_profit

        mp = [[0 for _ in range(n)] for _ in range(2)]
        mp[1][0] = -prices[0]
        for i in range(1, n):
            mp[0][i] = 0
            mp[1][i] = max(-prices[i], mp[1][i-1])

        for i in range(1, k+1):
            mp2 = [[0 for _ in range(n)] for _ in range(2)]
            mp2[1][0] = -prices[0]
            for j in range(1, n):
                # 状态转移方程
                # 拥有0股：什么都不做，或者卖出一股
                mp2[0][j] = max(mp2[0][j-1], mp[1][j-1] + prices[j])
                # 拥有1股：什么都不做，或者买入一股
                mp2[1][j] = max(mp2[1][j-1], mp2[0][j-1] - prices[j])
            mp = mp2

        return mp[0][-1]


class Solution1:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k == 0:
            return 0
        n = len(prices)
        if k >= n / 2:
            return sum(a - b for a, b in zip(prices[1:], prices[:-1]) if a > b)
        local_max = [0] * (k + 1)
        global_max = [0] * (k + 1)
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            for j in range(k, 0, -1):
                local_max[j] = max(local_max[j], global_max[j - 1]) + diff
                global_max[j] = max(local_max[j], global_max[j])
        return global_max[k]