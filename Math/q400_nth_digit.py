# Time:  O(n)
# Space: O(1)

# 解题思路：
# 寻找规律
# 1-9     9*1
# 10-99   90*2
# 100-999 900*3
# 拆分为计算所求数以及其偏移量


class Solution:
    def findNthDigit(self, n: 'int') -> 'int':
        k, base = 1, 9
        # 从1开始计数，减去1简化计算
        n -= 1
        while n >= k * base:
            n -= k * base
            base *= 10
            k += 1

        a, b = divmod(n, k)
        return int(str(10 ** (k - 1) + a)[b])
