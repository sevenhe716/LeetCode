# Time:  O(n)
# Space: O(n)

# Ideas:
# reverse all and reverse every words, or just use lib


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])
