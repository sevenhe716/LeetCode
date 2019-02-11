# Time:  O(n)
# Space: O(1)

# 解题思路：
# 异或是不进位的加法，与得出所有需要进位的位，但是只能应用于两个正数的加法


class Solution:
    # 只能应用于两个正数相加
    def getSum1(self, a: 'int', b: 'int') -> 'int':
        print(bin(a & 0b1111111111111111), bin(b & 0b1111111111111111))
        while a != 0:
            a, b = (a & b) << 1, a ^ b
            print(bin(a & 0b1111111111111111), bin(b & 0b1111111111111111))
        return b

    def getSum(self, a: 'int', b: 'int') -> 'int':
        INT32_MAX = 0x7FFFFFFF
        INT32_MIN = 0x80000000

        # mask to get last 32 bits
        MASK = 0xFFFFFFFF

        while a != 0:
            a, b = ((a & b) << 1) & MASK, (a ^ b) & MASK
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return b if b <= INT32_MAX else ~(b ^ MASK)
