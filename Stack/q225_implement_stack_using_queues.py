# Time:  O(n)
# Space: O(1)

# 解题思路：
# 用两个队列来实现栈
from collections import deque
from functools import reduce


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queues = [deque(), deque()]
        self.cur_index = 0

    def push(self, x: 'int') -> 'None':
        """
        Push element x onto stack.
        """
        self.queues[self.cur_index].append(x)
        if len(self.queues[self.cur_index]) > 1:
            self.queues[1 - self.cur_index].append(self.queues[self.cur_index].popleft())

    def pop(self) -> 'int':
        """
        Removes the element on top of the stack and returns that element.
        """
        res = self.queues[self.cur_index].popleft()
        while len(self.queues[1 - self.cur_index]) > 1:
            self.queues[self.cur_index].append(self.queues[1 - self.cur_index].popleft())
        self.cur_index = 1 - self.cur_index
        return res

    def top(self) -> 'int':
        """
        Get the top element.
        """
        return self.queues[self.cur_index][0]

    def empty(self) -> 'bool':
        """
        Returns whether the stack is empty.
        """
        # return len(self.queues[0]) + len(self.queues[1]) == 0
        return not self.queues[0] and not self.queues[1]
        # return reduce(lambda x, y: x + len(y), self.queues, 0) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
