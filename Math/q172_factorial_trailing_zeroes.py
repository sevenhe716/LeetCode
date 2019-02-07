# Time:  O(n)
# Space: O(1)

# 解题思路：
# 每有一个10的因子(相当于一个5)，则产生一个0，每有一个5的因子（同时至少产生偶数）也产生一个0
# 实际就是分解质因数之后5的个数，也就是n // 5^k = m则，有m*k个0，再求和即可


class Solution:
    # 超时
    def trailingZeroes1(self, n: 'int') -> 'int':
        def count5(n):
            count = 0
            while n > 0 and n % 5 == 0:
                count += 1
                n = n // 5
            return count

        res = 0
        for i in range(0, n + 1, 5):
            res += count5(i)
        return res

    # 优化思路，除5^n求和
    def trailingZeroes(self, n: 'int') -> 'int':
        res, five_factor = 0, 5
        while five_factor <= n:
            res += n // five_factor
            five_factor *= 5
        return res


class Solution1:
    # 递归的写法更精炼
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)