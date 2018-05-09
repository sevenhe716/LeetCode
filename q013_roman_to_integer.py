# Time:  O(n)
# Space: O(1)

# 解题思路：
# 把罗马数字对应的数字相加即可，需要先特殊处理4和9

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        special_nums = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']      # 优先执行检查的特殊罗马数字，4和9
        convert_map = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                       'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        num = 0

        for special_num in special_nums:
            if special_num in s:
                num += convert_map[special_num]
                i = s.index(special_num)
                s = s[:i] + s[i+2:]

        for ch in s:
            num += convert_map[ch]

        return num


# 寻找规律，4和9的特征是s[i]>s[i - 1]，检测到后减去双倍的s[i-1]即可(因为前面已经加过了一次s[i-1]了，所以要减两次)
class Solution1:
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal


# 倒序遍历，同样发现4和9的特征后，从加变成减即可
class SolutionF:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        pre = 0
        length = len(s)
        i = length - 1
        while i >= 0:
            value = roman_dict[s[i]]
            if value >= pre:
                result += value
            else:
                result -= value
            pre = value
            i -= 1
        return result

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
# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
