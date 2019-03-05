# Time:  O(n)
# Space: O(1)

# 解题思路：
# 只是求一次有效操作之后的所有情况，似乎跟游戏规则以及最终字符串没有关系


class Solution:
    def generatePossibleNextMoves(self, s: str) -> 'List[str]':
        res = []
        for i in range(len(s) - 1):
            if s[i] == s[i+1] == '+':
                res.append(s[:i] + '--' + s[i+2:])
        return res
