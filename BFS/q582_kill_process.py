# Time:  O(n)
# Space: O(1)

# 解题思路：
# BFS
from collections import defaultdict


class Solution:
    def killProcess(self, pid: 'List[int]', ppid: 'List[int]', kill: int) -> 'List[int]':
        self.res, self.kills = [], [kill]
        # 建索引加速查询
        ppid_pid = defaultdict(list)
        for p1, p2 in zip(pid, ppid):
            ppid_pid[p2].append(p1)
        # bfs
        while self.kills:
            kill = self.kills.pop()
            self.res.append(kill)
            self.kills += ppid_pid[kill]
        return self.res


class Solution1:
    # pythonic
    def killProcess(self, pid, ppid, kill):
        d = defaultdict(list)
        for c, p in zip(pid, ppid):
            d[p].append(c)
        bfs = [kill]
        for i in bfs:
            bfs += d[i]
        return bfs
