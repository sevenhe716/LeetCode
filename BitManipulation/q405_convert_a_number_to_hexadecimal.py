# Time:  O(n)
# Space: O(1)

# 解题思路：
# 负数为正数取反再加1


class Solution:
    def toHex(self, num: 'int') -> 'str':
        letter_map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        if num == 0:
            return '0'
        if num < 0:
            # mask = int('ffffffff', 16)
            mask = 4294967295
            num = (mask ^ -num) + 1
        ans = ''
        while num > 0:
            num, r = divmod(num, 16)
            ans = letter_map[r] + ans
        return ans


class Solution1:
    # 负数也满足
    def toHex(self, num: 'int') -> 'str':
        ans = ""
        for _ in range(8):
            num, r = divmod(num, 16)
            print(num, r)
            ans = "0123456789abcdef"[r] + ans
            if num == 0:
                break
        return ans