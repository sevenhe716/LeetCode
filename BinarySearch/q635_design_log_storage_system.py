# Time:  O(n)
# Space: O(n)

# 解题思路：
# 首先存储结构应该支持随机访问，然后是有序结构，最好支持O(log(n))时间复杂度的插入和删除，跳表？红黑树？
import bisect


class LogSystem:
    def __init__(self):
        self.logs = []
        self.start = '2000:01:01:00:00:00'
        self.end = '2017:12:31:23:59:59'
        self.gra_idx = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    # O(logn) to search, O(n) to insert, so skip list or black-red tree is better solution
    def put(self, id: int, timestamp: str) -> None:
        bisect.insort_left(self.logs, (timestamp, id))

    # O(logn)
    def retrieve(self, s: str, e: str, gra: str) -> 'List[int]':
        idx = self.gra_idx[gra]
        lo = bisect.bisect_left(self.logs, (s[:idx] + self.start[idx:], 0))
        hi = bisect.bisect_right(self.logs, (e[:idx] + self.end[idx:], 300))
        return [log[1] for log in self.logs[lo:hi]]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

# elegant but slow
class LogSystem1:
    def __init__(self):
        self.times = []
        self.g = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id, timestamp):
        self.times.append([timestamp, id])

    def retrieve(self, s, e, gra):
        ind = self.g[gra]
        s, e = s[:ind], e[:ind]
        return [i for time, i in self.times if s <= time[:ind] <= e]