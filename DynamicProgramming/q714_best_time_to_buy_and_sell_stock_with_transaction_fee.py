# Time:  O(n)
# Space: O(1)

# 解题思路：
# 可以用常规的动态规划，也可以尝试下贪心的思路
# 动态规划：
# 我的思路，如果用贪心只会考虑短期的利益，如1 4 3 6，因为1->4 3->6为正，则会选择这种局部最优，而非1-6全局最优
# 实际不然，用cash hold两种状态同时维护求最大值，贪心算法是全局最优解

class Solution:
    # 超时
    def maxProfit1(self, prices: 'List[int]', fee: 'int') -> 'int':
        if not prices:
            return 0

        n = len(prices)
        # 只当前那天卖出的最大利润，这样是不行的，因为不限制购买次数，无法标记出每次买入和卖出的状态
        # 状态定义：考虑标记K次交易，每次都计算交易费用，但是K没有上限，可能需要遍历到n-1，最高交易次数，或者是直到不再产生更高利润时。
        mp = [[0 for _ in range(n)] for _ in range(2)]
        mp[1][0] = -prices[0]
        for i in range(1, n):
            mp[0][i] = 0
            mp[1][i] = max(-prices[i], mp[1][i - 1])

        max_profit = 0
        for i in range(1, n):
            mp2 = [[0 for _ in range(n)] for _ in range(2)]
            mp2[1][0] = -prices[0]
            for j in range(1, n):
                # 状态转移方程
                # 拥有0股：什么都不做，或者卖出一股
                mp2[0][j] = max(mp2[0][j - 1], mp[1][j - 1] + prices[j] - fee)
                # 拥有1股：什么都不做，或者买入一股
                mp2[1][j] = max(mp2[1][j - 1], mp2[0][j - 1] - prices[j])
            mp = mp2
            if max_profit < mp[0][-1]:
                max_profit = mp[0][-1]
            else:
                return max_profit

        return max_profit

    def maxProfit(self, prices: 'List[int]', fee: 'int') -> 'int':
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])

        return cash

class Solution1:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        res = 0
        min_val = prices[0]
        for ele in prices[1:]:
            if ele < min_val:
                min_val = ele
            elif ele > min_val + fee:
                res += ele - fee - min_val
                min_val = ele - fee             # 更新当前最小值，需减去手续费，防止多次扣费
        return res