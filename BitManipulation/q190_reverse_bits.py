# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits1(self, n):
        return int(bin(n)[2::].zfill(32)[::-1], 2)

    def reverseBits(self, n):
        mask, res = 1 << 31, 0
        for i in range(32):
            if n & 1:
                res |= mask
            mask >>= 1
            n >>= 1
        return res
