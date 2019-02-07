# Time:  O(n)
# Space: O(1)

# 解题思路：
# cool-down 有一天的cd，且可以购买无限次，那么状态定义为当天有出售的最大利润，同样需要记录购买和售出，以及CD情况


class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0

        n = len(prices)
        # dp状态定义: 0 当前未持有，且CD已好，可以买入 1 当前持有，可以出售 2:今天刚出售，CD中
        # mp = [[0 for _ in range(n)] for _ in range(3)]
        # mp[1][0] = -prices[0]

        mp1 = [0] * 3
        mp1[1] = -prices[0]
        mp2 = [0] * 3
        for i in range(1, n):
            mp2[0] = max(mp1[0], mp1[2])  # 不动，或者CD转好
            mp2[1] = max(mp1[1], mp1[0] - prices[i])  # 不动，或者买入
            mp2[2] = mp1[1] + prices[i]  # 卖出
            # mp[0][i] = max(mp[0][i-1], mp[2][i-1])  # 不动，或者CD转好
            # mp[1][i] = max(mp[1][i-1], mp[0][i-1] - prices[i])  # 不动，或者买入
            # mp[2][i] = mp[1][i-1] + prices[i]   # 卖出
            mp1, mp2 = mp2, mp1

        return max(mp1[0], mp1[2])
