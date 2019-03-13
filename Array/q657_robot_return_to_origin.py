# Time:  O(n)
# Space: O(1)

# 解题思路：
#
import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        dir_dict = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
        for move in moves:
            pos[0] += dir_dict[move][0]
            pos[1] += dir_dict[move][1]
        return pos[0] == 0 and pos[1] == 0


class Solution1:
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

    def judgeCircle2(self, moves):
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']