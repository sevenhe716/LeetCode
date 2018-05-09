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


# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true
