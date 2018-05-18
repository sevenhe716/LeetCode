# Time:  O(n)
# Space: O(1)

# 解题思路：
# 取模再拼接字符串即可，为了考虑效率，未使用递归而且用list代替字符串拼接


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        str_list = []

        if not num:
            return '0'

        neg = True if num < 0 else False
        num = abs(num)

        while num != 0:
            num, remain = divmod(num, 7)
            str_list.insert(0, str(remain))

        if neg:
            return '-' + ''.join(str_list)
        else:
            return ''.join(str_list)


# recursion
class SolutionF:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:         # 负数可以直接加上符号，并且化归为正数
            return '-' + str(self.convertToBase7(-num))
        elif num < 7:
            return str(num)
        else:
            return str(self.convertToBase7(num//7)) + str(num % 7)
