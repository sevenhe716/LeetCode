# Time:  O(n)
# Space: O(1)

# 解题思路：
# 主要问题在于popMax，一个可行但效率不算太高的做法是，查找并删除popMax，时间复杂度为O(n)，pop出最大值之后重新寻找最大值时间复杂度也是O(n)
# 如果额外维护一个大顶堆，记录最大值以及其在stack中的索引位置，用于加速peekMax()和popMax()，但是pop的时候也需要维护大顶堆
# 优化思路：可以利用max_stack，同时存储最大值及索引位置，使得pop的开销降为O(1)，同时也能快速定位到最大值的位置，在最大值弹出时，需要维护一次最大值之后的状态


# 这里默认调用均合法，暂不做防御型编程
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_val = float('-inf')

    # O(1)
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x > self.max_val:
            self.max_val = x

    # 通常O(1)，弹出最大值时O(n)
    def pop(self) -> int:
        res = self.stack.pop()
        if res == self.max_val:
            self.max_val = max(self.stack) if self.stack else float('-inf')
        return res

    # O(1)
    def top(self) -> int:
        return self.stack[-1]

    # O(1)
    def peekMax(self) -> int:
        return self.max_val

    # O(n)
    def popMax(self) -> int:
        # python list没有findex或rfind，两种修改方法
        # 1. 翻转remove再翻转
        # stack_reverse = self.stack[::-1]
        # stack_reverse.remove(self.max_val)
        # self.stack = stack_reverse[::-1]
        # 2. 找到index后slice拼接
        res = self.max_val
        index = len(self.stack) - 1 - self.stack[::-1].index(res)
        self.stack = self.stack[:index] + self.stack[index+1:]
        self.max_val = max(self.stack) if self.stack else float('-inf')
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


class MaxStack1:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []

    def push(self, x: 'int') -> 'None':
        self.stack.append(x)
        if len(self.max_stack) == 0 or x >= self.max_stack[-1][0]:
            self.max_stack.append((x, len(self.stack)-1))

    def pop(self) -> 'int':
        if self.max_stack[-1][1] == len(self.stack) - 1:
            self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> 'int':
        return self.stack[-1]

    def peekMax(self) -> 'int':
        return self.max_stack[-1][0]

    def popMax(self) -> 'int':
        val, pos = self.max_stack.pop()
        del self.stack[pos]
        # 最大值以后的值中寻找新的最大值序列添加到stack中
        for i in range(pos, len(self.stack)):
            x = self.stack[i]
            if len(self.max_stack) == 0 or x >= self.max_stack[-1][0]:
                self.max_stack.append((x, i))
        return val