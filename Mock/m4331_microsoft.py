# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def convertToTitle(self, n: int) -> str:
        num_letter = {i + 1: chr(ord('A') + i) for i in range(26)}
        res = ''
        while n > 0:
            n -= 1
            n, r = divmod(n, 26)
            res = num_letter[r+1] + res

        return res
