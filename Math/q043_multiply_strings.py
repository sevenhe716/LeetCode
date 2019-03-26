# Time:  O(n)
# Space: O(1)

# 解题思路：
# must not convert the inputs to integer directly
# 不知道这个限定条件限定到什么程度，肯定是允许转成int来计算基本的加乘法的，这里默认允许转一个数字


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, index = int(num1), len(num2)-1
        base, result = 1, 0

        while index >= 0:
            result += int(num2[index]) * n1 * base
            base *= 10
            index -= 1

        return str(result)


# https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
class Solution1:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        pos = [0]*(m+n)

        ord_zero = ord('0')
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = (ord(num1[i]) - ord_zero) * (ord(num2[j]) - ord_zero)
                p1, p2 = i + j, i + j + 1
                sum = mul + pos[p2]

                pos[p1] += sum // 10
                pos[p2] = sum % 10      # 不加等吗?只有保证是第一次赋值时才能用等于

        num_str = []
        for i in range(m + n):
            if not (pos[i] == 0 and len(num_str) == 0):
                num_str.append(str(pos[i]))

        # return ''.join(num_str) if num_str else '0'
        return ''.join(num_str)

    def multiply1(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2))
        pos = len(product) - 1

        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                product[tempPos] += int(n1) * int(n2)
                # 这里不需要考虑连续进位的问题，因为product中存的数可以大于9
                product[tempPos], r = divmod(product[tempPos], 10)
                product[tempPos - 1] += r
                tempPos -= 1
            pos -= 1

        res = ''.join(map(str, product)).lstrip('0')
        return res if res != '' else '0'