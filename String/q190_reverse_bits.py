# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2::].zfill(32)[::-1], 2)
