# Time:  O(log(n))
# Space: O(1)

# 解题思路：
# 维护十进制的迭代器，进行累加即可，由于python3的int是任意精度的，所以需要人工判断越界问题
# 特殊情况处理：
# 1. 反转后32位有符号整数溢出问题
# 2. 32位有符号数的取值范围是-2147483648~2147483647，-2147483648符号反转之后直接溢出（对于C++ int32而言，python3不会）


class Solution:
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1 if x >= 0 else -1  # 取值范围为-2147483648~2147483647，python3整型无长度限制，反转不会导致问题
        x *= sign
        y = 0

        while x != 0:
            remain = x % 10
            x = (x - remain) // 10
            y = y * 10 + remain

        y *= sign

        if y < -2147483648 or y > 2147483647:  # -(1 << 31), (1 << 31) - 1
            return 0
        else:
            return y

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result if result <= 0x7fffffff else 0  # Handle overflow.

    def reverse3(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1])
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 1 if x >= 0 else -1  # s = cmp(x, 0)
        r = int(repr(s * x)[::-1])
        return s * r * (r < 2 ** 31)