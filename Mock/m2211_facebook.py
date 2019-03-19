# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ''.join(c for c in s.lower() if c.isalpha() or c.isdigit())
        # alphanumeric = ''.join(str.isalpha or str.isdigit, list(s.lower())))
        return alphanumeric == alphanumeric[::-1]