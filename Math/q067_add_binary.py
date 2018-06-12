# Time:  O(n)
# Space: O(1)

# 解题思路：
# 二进制加法，这里尝试hashmap查表法，当然也可以转为int做加法


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        x = [int(c) for c in a]
        y = [int(c) for c in b]

        # 统一a为短的数，方便后续讨论
        if len(x) > len(y):
            x, y = y, x

        carry = 0
        for i in range(len(x)):
            y[~i] = x[~i] + y[~i] + carry
            if y[~i] >= 2:
                y[~i] -= 2
                carry = 1
            else:
                carry = 0

        i = len(x)
        while i < len(y) and carry:
            y[~i] = y[~i] + carry
            if y[~i] >= 2:
                y[~i] -= 2
                carry = 1
            else:
                carry = 0
            i += 1

        if carry:
            y.insert(0, 1)

        return ''.join([str(c) for c in y])


    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = list(a)
        b = list(b)

        add = {
            ('0', '0', '0'): ('0', '0'),
            ('0', '0', '1'): ('0', '1'),
            ('0', '1', '0'): ('0', '1'),
            ('0', '1', '1'): ('1', '0'),
            ('1', '0', '0'): ('0', '1'),
            ('1', '0', '1'): ('1', '0'),
            ('1', '1', '0'): ('1', '0'),
            ('1', '1', '1'): ('1', '1')
        }

        # 统一a为短的数，方便后续讨论
        if len(a) > len(b):
            a, b = b, a

        carry = '0'
        for i in range(len(a)):
            carry, b[~i] = add[(a[~i], b[~i], carry)]

        i = len(a)
        while i < len(b) and carry == '1':
            carry, b[~i] = add['0', b[~i], carry]
            i += 1

        if carry == '1':
            b.insert(0, '1')

        return ''.join(b)


class SolutionF:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2)+int(b, 2))[2:]
