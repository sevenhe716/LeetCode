# Time:  O(n)
# Space: O(1)

# Ideas:
# two-pointer?


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        def valid(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while left <= right:
            if s[left] != s[right]:
                if valid(left+1, right) or valid(left, right-1):
                    return True
                else:
                    return False
            left += 1
            right -= 1

        return True
