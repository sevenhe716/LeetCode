# Time:  O(n^2)
# Space: O(1)

# Ideas:
# two pointer?


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = ''
        for i in range(len(s)):
            left = right = i
            while 0 <= left <= right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            left += 1
            right -= 1

            if right - left + 1 > max_len:
                max_len = right - left + 1
                res = s[left:right + 1]

            left, right = i, i + 1
            while 0 <= left < right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            left += 1
            right -= 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
                res = s[left:right + 1]

        return res

