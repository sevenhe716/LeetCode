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