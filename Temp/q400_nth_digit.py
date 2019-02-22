# Time:  O(n)
# Space: O(1)

# 解题思路：
# 1-9     9*1
# 10-99   90*2
# 100-999 900*3
# 拆分为找到那个数以及其偏移量


class Solution:
    def findNthDigit(self, n: 'int') -> 'int':
        k = 1
        base = 9
        total = 1
        num = n

        while n > k * base:
            total += base
            num -= (k - 1) * base
            base *= 10
            k += 1
            # total += k * base
        print(num, k, base, total)
        i, r = divmod(num - total-1, k)
        num = i + total
        print(num, r)
        return int(str(num)[r])
