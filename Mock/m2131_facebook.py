# Time:  O(n)
# Space: O(1)

# Ideas:
#


class Solution:
    def romanToInt(self, s: str) -> int:
        s_v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i, c in enumerate(s):
            if i + 1 < len(s) and s_v[c] < s_v[s[i + 1]]:
                res -= s_v[c]
            else:
                res += s_v[c]
        return res

    # def romanToInt(self, s: str) -> int:
    #     def generate(num, one, five, ten):
    #         if num < 4:
    #             return one * num
    #         elif num == 4:
    #             return one + five
    #         elif num < 9:
    #             return five + one * (num - 5)
    #         else:
    #             return one + ten
    #
    #
    #     generate('I', 'V', 'X')
