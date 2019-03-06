# Time:  O(n)
# Space: O(n)

# 解题思路：
# 需要支持同一秒hit数很大的情况，因此用计数器来存储每秒的计数，固定统计前5分钟的计数，因此循环队列比较适合
# 分情况分割区间的写法吃力不讨好，直接遍历赋值比较好，唯一区别就是当索引超出时回到原点即可
# 优化：之前的解法相当于分桶计数，当数据不是太密集的时候，时空复杂度太高，用队列比较适合，也可以考虑用字典
# 用字典统计的效率跟我的解法一样低，只是空间占用更小，而且对于实际生产应用，需要定时进行清理
from collections import defaultdict
from bisect import bisect_right


class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 300
        self.counter = [0] * self.size
        self.next, self.cur_time = 1, 1

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        diff = timestamp - self.cur_time

        if diff >= self.size:
            self.counter = [0] * self.size
        else:
            diff2 = self.size - self.next - diff
            if diff2 > 0:
                self.counter[self.next:self.next + diff] = [0] * diff
            else:
                self.counter[self.next:] = [0] * (self.size - self.next)
                self.counter[:-diff2] = [0] * -diff2
            self.next = (self.next + diff) % self.size
        self.cur_time = timestamp
        if self.next > 0:
            self.counter[self.next - 1] += 1
        else:
            self.counter[-1] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        diff = self.size + self.cur_time - timestamp
        if diff <= 0:
            return 0
        else:
            diff2 = diff - self.next
            if diff2 <= 0:
                return sum(self.counter[-diff2:self.next])
            else:
                return sum(self.counter[:self.next]) + sum(self.counter[self.size - diff2:])


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)


# dict solution
class HitCounter1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = defaultdict(int)

    def hit(self, timestamp: 'int') -> 'None':
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp in self.hits:
            self.hits[timestamp] += 1
        else:
            self.hits[timestamp] = 1

        # 定时清理
        # past = [ts for ts in self.hits if ts < timestamp - 300]
        # for ts in past:
        #     del self.hits[ts]

    def getHits(self, timestamp: 'int') -> 'int':
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        return sum(self.hits[ts] for ts in range(timestamp, timestamp - 300, -1) if ts > 0)


# bisect queue
class HitCounter2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timed_counter = [[0, 0]]

    def hit(self, timestamp: 'int') -> 'None':
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.timed_counter[-1][0] == timestamp:
            self.timed_counter[-1][1] += 1
        else:
            prev_count = self.timed_counter[-1][1]
            self.timed_counter.append([timestamp, prev_count + 1])

    def getHits(self, timestamp: 'int') -> 'int':
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        t_begin, t_end = timestamp - 300, timestamp
        c_begin, c_end = self._search(t_begin), self._search(t_end)
        return c_end - c_begin

    def _search(self, ts):
        i, j = 0, len(self.timed_counter),
        k = -1
        while i < j:
            k = (i + j) // 2
            if self.timed_counter[k][0] > ts:
                j = k
            elif self.timed_counter[k][0] < ts:
                i = k + 1
            else:
                break
        else:
            k = i - 1
        if k < 0:
            return 0
        else:
            return self.timed_counter[k][1]


# bucket solution
class HitCounter3(object):
    def __init__(self):
        self.window_size = 300
        self.buckets = [None] * self.window_size

    def hit(self, timestamp):
        index = timestamp % self.window_size
        if self.buckets[index] is None:
            self.buckets[index] = [timestamp, 1]
            return

        old_time, old_count = self.buckets[index]
        if old_time < timestamp:
            self.total -= old_count
            self.buckets[index] = [timestamp, 1]
        else:  # old time is equal to the timestamp
            self.buckets[index][1] += 1

    def getHits(self, timestamp):
        total = 0
        for bt in self.buckets:
            if bt and timestamp - bt[0] < self.window_size:
                total += bt[1]
        return total


# 这个解法比较简洁，但问题在于没使用计数器，不适用于密集数据
class HitCounter:
    def __init__(self):
        self.coll = []

    def hit(self, timestamp):
        self.coll.append(timestamp)

    def getHits(self, timestamp):
        lo = bisect_right(self.coll, timestamp - 300)
        ## safely can remove old elems, since new query will have greater timestamp
        self.coll = self.coll[lo:]
        return len(self.coll)

# 支持lambda key的bisect
# class KeyifyList(object):
#     def __init__(self, inner, key):
#         self.inner = inner
#         self.key = key
#
#     def __len__(self):
#         return len(self.inner)
#
#     def __getitem__(self, k):
#         return self.key(self.inner[k])
#
#
# if __name__ == '__main__':
#     import bisect
#     L = [(0, 0), (1, 5), (2, 10), (3, 15), (4, 20)]
#     assert bisect.bisect_left(KeyifyList(L, lambda x: x[0]), 3) == 3
#     assert bisect.bisect_left(KeyifyList(L, lambda x: x[1]), 3) == 1
