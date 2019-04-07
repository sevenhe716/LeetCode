# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join([x for x in s if x.isalpha() or x.isnumeric()])

        return s == s[::-1]

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ''.join(c for c in s.lower() if c.isalpha() or c.isdigit())
        return alphanumeric == alphanumeric[::-1]