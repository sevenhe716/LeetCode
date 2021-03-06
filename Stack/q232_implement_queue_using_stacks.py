# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack, self.pop_stack = [], []

    def push(self, x: 'int') -> 'None':
        """
        Push element x to the back of queue.
        """
        while self.pop_stack:
            self.push_stack.append(self.pop_stack.pop())
        self.push_stack.append(x)

    def pop(self) -> 'int':
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> 'int':
        """
        Get the front element.
        """
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self) -> 'bool':
        """
        Returns whether the queue is empty.
        """
        return len(self.push_stack) + len(self.pop_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()