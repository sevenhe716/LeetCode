# Time:  O(n)
# Space: O(1)

# 解题思路：
# 动态规划：状态定义以当前位置作为开头的解码数，倒序遍历
# 特殊情况就是以1开头或2开头下一位小于等于6，以及0的情况
# dp空间优化：只需要存储上一个值即可
from functools import reduce


class Solution:
    # 暂时不考虑验证输入的合法性，合法性验证即0的左边一定是1或2
    def numDecodings(self, s: 'str') -> 'int':
        # 合法性验证：
        for i, c in enumerate(s):
            if c == '0' and (i == 0 or (s[i - 1] != '1' and s[i - 1] != '2')):
                return 0

        if len(s) <= 1:
            return len(s)

        def check(i):
            # ASCII满足比较性
            # return s[i+1] != '0' and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'))
            return s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')

        dp = [1] * len(s)

        if s[-1] != '0' and check(-2):
            dp[-2] = 2
        else:
            dp[-2] = 1

        for i in range(len(s))[-3::-1]:
            # 单独讨论0，在已经验证合法性的情况下，如果当前是0，或者右侧，再右侧是0，则只存在一种分割情况
            if s[i] == '0':
                dp[i] = dp[i + 1]
            elif s[i + 1] != '0' and s[i + 2] != '0' and check(i):
                dp[i] = dp[i + 1] + (dp[i + 2] if check(i + 1) else dp[i + 1])
            else:
                dp[i] = dp[i + 1]

        return dp[0]


class Solution1:
    def numDecodings(self, s: str) -> int:
        if len(s) > 0 and s[0] > '0':
            a, b = 1, 1
        else:
            return 0
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] > '2' or s[i - 1] == '0':
                    return 0
                a, b = 0, a
            elif s[i - 1] == '1' or (s[i - 1] == '2' and s[i] < '7'):
                a, b = b, a + b
            else:
                a, b = b, b
        return b

    # def numDecodings(self, s):
    #     return reduce(lambda (v, w, p), d: (w, (d > '0') * w + (9 < int(p + d) < 27) * v, d), s, (0, s > '', ''))[1] * 1

    def numDecodings2(self, s):
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w
