# Time:  O(n*amount)
# Space: O(amount)

# 解题思路：
# 动态规划


class Solution:
    def coinChange(self, coins: 'List[int]', amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
        return dp[-1] if dp[-1] != float('inf') else -1


class Solution1:
    # 4 lines
    def coinChange(self, coins: 'List[int]', amount: int) -> int:
        dp = [0]
        for i in range(1, amount + 1):
            dp += [min([dp[i - x] + 1 for x in coins if i - x >= 0 and dp[i - x] >= 0] or [-1])]
        return dp[-1]

    # BFS
    def coinChange1(self, coins: 'List[int]', amount: int) -> int:
        if amount == 0:
            return 0
        value1, value2, nc = [0], [], 0
        visited = [False] * (amount + 1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    new_val = v + coin
                    if new_val == amount:
                        return nc
                    elif new_val > amount:
                        continue
                    elif not visited[new_val]:
                        visited[new_val] = True
                        value2.append(new_val)
            value1, value2 = value2, []
        return -1

    def coinChange2(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else MAX for c in coins) + 1

        # more pythonic, bool作为下标
        return [dp[-1], -1][dp[-1] == MAX]
