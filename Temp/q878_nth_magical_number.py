# Time:  O(n)
# Space: O(1)

# 解题思路：
#


class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """

        def lcm(x, y):
            lcms = [0]

            x1, y1 = x, y

            while True:
                if x1 == y1:
                    return x1, lcms
                if x1 < y1:
                    lcms.append(x1)
                    x1 += x
                else:
                    lcms.append(y1)
                    y1 += y

            return lcm, lcms

        # def gcd(m, n):
        #     if not n:
        #         return m
        #     else:
        #         return gcd(n, m % n)
        #
        # def LCM(m, n):
        #     if m * n == 0:
        #         return 0
        #     return int(m * n / gcd(m, n))

        l, lcms = lcm(A, B)
        # print(lcms)
        step = len(lcms)

        count = N // step
        ans = l * count + lcms[N % step]
        return ans % (10 ** 9 + 7)
