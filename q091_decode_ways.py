# Time:  O(n)
# Space: O(1)

# 解题思路：
# 动态规划：状态定义以当前位置作为开头的解码数，倒序遍历
# 特殊情况就是以1开头或2开头下一位小于等于6，以及0的情况


class Solution:
    # 暂时不考虑验证输入的合法性，合法性验证即0的左边一定是1或2
    def numDecodings(self, s: 'str') -> 'int':
        # 合法性验证：
        for i, c in enumerate(s):
            if c == '0' and (i == 0 or (s[i-1] != '1' and s[i-1] != '2')):
                return 0

        if len(s) <= 1:
            return len(s)

        def check(i):
            # ASCII满足比较性
            return s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')

        dp = [1] * len(s)
        dp[-2] = 2 if check(len(s)-2) else 1
        for i in range(len(s))[-3::-1]:
            if check(i):
                if s[i+1] == '0':
                    dp[i] = dp[i+1]
                else:
                    dp[i] = dp[i+1] + (dp[i+2] if check(i+1) else dp[i+1])
            else:
                dp[i] = dp[i+1]

        return dp[0]
