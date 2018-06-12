# Time:  O(n)
# Space: O(1)

# 解题思路：
# 主要考察是否考虑到各种数字表达方式，如去前后的空格，+-号，小数，科学表达方式(前面是小数e后面是整数)，
# 是否还要考虑二八十六进制表达方式，以及0开头的问题
# 正则表达式


class Solution:
    def isNumber1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re

        s = s.strip()
        if not s:
            return False

        return True if re.fullmatch(r'[+|-]?(([1-9]+[0-9]*)|0)?(\.[0-9]+)?(e[0-9]+)?', s) else False

    def isNumber(self, s):
        import re
        if not s:
            return False
        p = r'^\s*[-+]?(\d+(\.\d*)?|\.\d+)(e[-+]?[0-9]+)?\s*$'
        m = re.match(p, s)
        return True if m else False
