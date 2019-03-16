# Time:  O(n)
# Space: O(1)

# Ideas:
# queue
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.total = 0
        self.cur_size = 0
        self.size = size

    def next(self, val: int) -> float:
        if self.cur_size >= self.size:
            self.total -= self.queue.popleft()
        else:
            self.cur_size += 1

        self.queue.append(val)
        self.total += val
        return self.total / self.cur_size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
