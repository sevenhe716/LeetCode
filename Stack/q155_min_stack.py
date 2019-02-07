# Time:  O(n)
# Space: O(1)

# 解题思路：
# 考虑把当前堆栈的最小值同时也压入栈


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.cur_min = 2147483647

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.cur_min = x if self.cur_min > x else self.cur_min
        self.stack.append((x, self.cur_min))

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()

        # 出栈后更新最小值
        if self.stack:
            self.cur_min = self.getMin()
        else:
            self.cur_min = 2147483647

    def top(self):
        """
        :rtype: int
        """
        # 防御性编程
        if not self.stack:
            return 0
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        # 防御性编程
        if not self.stack:
            return 0
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0

    def push(self, x: 'int') -> 'None':
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self) -> 'None':
        if self.stack:
            pop = self.stack.pop()
            if pop < 0:
                self.min = self.min - pop

    def top(self) -> 'int':
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> 'int':
        return self.min
