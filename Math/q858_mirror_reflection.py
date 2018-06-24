# Time:  O(n)
# Space: O(1)

# 解题思路：
# reflection simulation


class Solution:
    # reflection simulation
    def mirrorReflection(self, p, q):
        # from math import isclose
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        # 归一化
        q = q / p
        p = 1.

        x1, y1 = 0., 0.
        x2, y2 = p, q

        def isclose(n1, n2):
            return -0.0001 < n1 - n2 < 0.0001

        # ax + b = y
        # 0: (1, 0), 1: (1, 1), 2: (0, 1)
        # a = (y1-y2)/(x1-x2), b = (x1y2 - x2y1)/(x1 - x2)
        def check():
            print(a+b)
            if isclose(a + b, 0.):
                return 0
            elif isclose(a + b, 1.):
                return 1
            elif isclose(b, 1.):
                return 2
            else:
                return -1

        # x=m对称 a = -a b = b + 2ma
        # y=n对称 a = -a b = -b + 2m
        def reflect():
            nonlocal a, b
            if isclose(x2, 0.) or isclose(x2, 1.):
                b = -b + 2 * y2
                a = -a
            elif isclose(y2, 0.) or isclose(y2, 1.):
                b = b + 2 * x2 * a
                a = -a
            else:
                print('wrong')

        def calc_formula():
            return (y1 - y2) / (x1 - x2), (x1 * y2 - x2 * y1) / (x1 - x2)

        def calc_point():
            # x = 0
            if not isclose(x2, 0):
                x, y = 0, b
                if 0 <= y <= 1:
                    return x, y

            # x = 1
            if not isclose(x2, 1):
                x, y = 1, a + b
                if 0 <= y <= 1:
                    return x, y

            # y = 0
            if not isclose(y2, 0):
                x, y = - b / a, 0
                if 0 <= x <= 1:
                    return x, y

            # y = 1
            if not isclose(y2, 1):
                x, y = (1 - b) / a, 1
                if 0 <= x <= 1:
                    return x, y

            return -1, -1

        # a, b = q, 0
        a, b = calc_formula()

        print(x1, y1, x2, y2)
        print(a, b)
        res = check()
        while isclose(res, -1.):
            reflect()
            print(a, b)
            x1, y1 = x2, y2
            x2, y2 = calc_point()
            print(x1, y1, x2, y2)
            # a, b = calc_formula()
            # print(a, b)
            res = check()
            print(res)
            print()

        return res


class Solution1:
    # math
    def mirrorReflection(self, p, q):
        # from math import isclose
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2

        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1

    def mirrorReflection1(self, p, q):
        len = q
        bounce = 0
        while len % p:
            len += q
            bounce += 1

        if bounce % 2:
            return 2
        elif (len // p) % 2 == 0:
            return 0
        else:
            return 1
