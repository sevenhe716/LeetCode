# Time:  O(n)
# Space: O(1)

# 解题思路：
# 用stack来维护bracket状态


class Solution:
    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {'(': ')', '{': '}', '[': ']'}

        stack = []
        for c in s:
            if c in bracket_map:
                stack.append(bracket_map[c])
            elif c in bracket_map.values():
                if stack:
                    test = stack.pop()
                    if test != c:
                        return False
                else:
                    return False
            else:
                return False

        return not stack

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {'(': ')', '{': '}', '[': ']'}

        stack = []
        for c in s:
            if c in bracket_map:
                stack.append(c)
            else:
                if not stack or bracket_map[stack.pop()] != c:
                    return False

        return not stack
