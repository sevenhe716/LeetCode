# Time:  O(n)
# Space: O(n)

# 解题思路：
# +需要记录最后两个数字，而C可以删除，如果有多个C的情况下，不知道应保留之前的多少个字符，因此记录所有字符是比较稳妥的办法


class Solution:
    def calPoints(self, ops: 'List[str]') -> int:
        scores = []
        res = 0

        for op in ops:
            if op == 'C':
                res -= scores.pop()
            elif op == 'D':
                scores.append(scores[-1] * 2)
                res += scores[-1]
            elif op == '+':
                scores.append(scores[-1] + scores[-2])
                res += scores[-1]
            else:
                scores.append(int(op))
                res += scores[-1]

        return res

