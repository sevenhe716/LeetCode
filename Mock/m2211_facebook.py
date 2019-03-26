# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def isPalindrome1(self, s: str) -> bool:
        alphanumeric = ''.join(c for c in s.lower() if c.isalpha() or c.isdigit())
        return alphanumeric == alphanumeric[::-1]

    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ''.join(filter(str.isalnum, s.lower()))
        return alphanumeric == alphanumeric[::-1]
