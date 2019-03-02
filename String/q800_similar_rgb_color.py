# Time:  O(n)
# Space: O(1)

# 解题思路：
# 选择距离8-bit数最近的0xXX
import bisect


class Solution:
    def similarRGB(self, color: str) -> str:
        res = '#'
        for i in range(1, len(color), 2):
            c1 = int(color[i:i+2], 16)
            c2 = int(color[i], 16)

            min_c2, min_similar = c2,  abs((c2 << 4) + c2 - c1)
            if c2 > 0:
                similar = abs((c2 - 1 << 4) + c2 - 1 - c1)
                if similar < min_similar:
                    min_c2 = c2 - 1
                    min_similar = similar
            if c2 < 15:
                similar = abs((c2 + 1 << 4) + c2 + 1 - c1)
                if similar < min_similar:
                    min_c2 = c2 + 1
            res += '{:0>2x}'.format((min_c2 << 4) + min_c2)
        return res


class Solution1(object):
    def similarRGB(self, color):
        def f(comp):
            q, r = divmod(int(comp, 16), 17)
            if r > 8: q += 1
            return '{:02x}'.format(17 * q)

        return '#' + f(color[1:3]) + f(color[3:5]) + f(color[5:])


class Solution2:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        code = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99',
                'aa', 'bb', 'cc', 'dd', 'ee', 'ff']

        def closest(color):
            pos = bisect.bisect(code, color)
            if pos == 0:
                return code[0]
            if pos == len(code):
                return code[-1]
            # 借鉴这个写法，lambda表达式寻找集合中的最小值
            res = min([pos - 1, pos], key=lambda x: abs(int(color, 16) - int(code[x], 16)))
            return code[res]

        return '#' + closest(color[1:3]) + closest(color[3:5]) + closest(color[5:7])