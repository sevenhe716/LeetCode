# Time:  O(n)
# Space: O(1)

# 解题思路：
# 队列，每次减去出列的值，再加上入列的值
# 优化：cur_size可以通过len得到
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = size
        self.cur_size = 0
        self.sum = 0

    def next(self, val: int) -> float:
        if self.cur_size < self.size:
            self.cur_size += 1
        else:
            self.sum -= self.queue.popleft()

        self.queue.append(val)
        self.sum += val

        return self.sum / self.cur_size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)