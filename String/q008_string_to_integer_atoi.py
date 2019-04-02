# Time:  O(n)
# Space: O(1)

# 解题思路：
# 实现atoi函数，应该是不能直接调用string to int的函数库，主要的关注点就是对于特殊情况的判断
# 去除空白，第一个非空字符判断，正负号，数字，表示范围越界的处理


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        str = str.strip()
        if len(str) == 0:
            return 0

        index = 0
        sign = 1

        if str[0] == '+':
            index += 1
        elif str[0] == '-':
            index += 1
            sign = -1

        num = 0

        while index < len(str) and ord('0') <= ord(str[index]) <= ord('9'):     # '0' <= str[i] <= '9'
            num = num * 10 + int(str[index])
            index += 1

        num *= sign

        num = min((1 << 31) - 1, num)
        num = max(-(1 << 31), num)

        return num


# 直接用正则表达式
class SolutionF:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re

        _max = 2147483647
        _min = -2147483648

        s = re.match('\s*[-\+]?\d+', str)
        if s:
            s = int(s.group())
            if s > _max:
                s = _max
            if s < _min:
                s = _min
            return s
        return 0