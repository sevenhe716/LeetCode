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


# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is
# found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have
# no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
# exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note: Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
# range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or
# INT_MIN (−231) is returned.
#
# Example 1:
#
# Input: "42"
# Output: 42
# Example 2:
#
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:
#
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:
#
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:
#
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.
