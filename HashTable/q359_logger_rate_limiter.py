# Time:  O(n)
# Space: O(1)

# 解题思路：
# 用dict缓存消息与时间戳，超过10秒的历史消息是否应该删除？否则空间占用率会越来越大比较好的方法是过一段时间再统一整理清除


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.mem or timestamp >= self.mem[message]:
            self.mem[message] = timestamp + 10
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)