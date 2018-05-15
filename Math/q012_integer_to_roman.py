# Time:  O(log(n))
# Space: O(1)

# 解题思路：
# 整体思路是转换成罗马的进制表示，需要特殊处理的是4和9

class Solution:
    def intToRoman1(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman = ''
        m, num = divmod(num, 1000)
        roman += 'M' * m  # 字符串拼接的效率不一定比list转string低

        c, num = divmod(num, 100)
        if c == 9:
            roman += 'CM'
        elif c == 4:
            roman += 'CD'
        elif c >= 5:
            roman += 'D' + 'C' * (c - 5)
        else:
            roman += 'C' * c

        x, num = divmod(num, 10)
        if x == 9:
            roman += 'XC'
        elif x == 4:
            roman += 'XL'
        elif x >= 5:
            roman += 'L' + 'X' * (x - 5)
        else:
            roman += 'X' * x

        if num == 9:
            roman += 'IX'
        elif num == 4:
            roman += 'IV'
        elif num >= 5:
            roman += 'V' + 'I' * (num - 5)
        else:
            roman += 'I' * num

        return roman

    # list version
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman = []
        m, num = divmod(num, 1000)
        roman.append('M' * m)

        c, num = divmod(num, 100)
        if c == 9:
            roman.append('CM')
        elif c == 4:
            roman.append('CD')
        elif c >= 5:
            roman.append('D')
            roman.append('C' * (c - 5))
        else:
            roman.append('C' * c)

        x, num = divmod(num, 10)
        if x == 9:
            roman.append('XC')
        elif x == 4:
            roman.append('XL')
        elif x >= 5:
            roman.append('L')
            roman.append('X' * (x - 5))
        else:
            roman.append('X' * x)

        if num == 9:
            roman.append('IX')
        elif num == 4:
            roman.append('IV')
        elif num >= 5:
            roman.append('V')
            roman.append('I' * (num - 5))
        else:
            roman.append('I' * num)

        return ''.join(roman)


# 把4和9也当作是模，这种方式值得借鉴
class Solution1(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", \
                       10: "X", 40: "XL", 50: "L", 90: "XC", \
                       100: "C", 400: "CD", 500: "D", 900: "CM", \
                       1000: "M"}
        keyset, result = sorted(numeral_map.keys()), []

        while num > 0:
            for key in reversed(keyset):
                while num / key > 0:
                    num -= key
                    result += numeral_map[key]

        return "".join(result)


# 最快的方式是建表，直接查表，用空间换时间
class SolutionF:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]


# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve
# is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not
# IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The
#  same principle applies to the number nine, which is written as IX. There are six instances where subtraction is
# used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: 3
# Output: "III"
# Example 2:
#
# Input: 4
# Output: "IV"
# Example 3:
#
# Input: 9
# Output: "IX"
# Example 4:
#
# Input: 58
# Output: "LVIII"
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# Example 5:
#
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
