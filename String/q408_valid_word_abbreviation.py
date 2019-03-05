# Time:  O(n)
# Space: O(1)

# 解题思路：
# 解析abbr，如果是数字则跳过多少个字符，如果是字符则检测匹配
# 特殊情况：当数字为0或以0开头时，是不合法的


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i1, i2, l1, l2 = 0, 0, len(word), len(abbr)
        while True:
            while abbr[i2].islower():
                if word[i1] != abbr[i2]:
                    return False
                i1, i2 = i1 + 1, i2 + 1
                if i1 == l1 and i2 == l2:
                    return True
                if i1 == l1 or i2 == l2:
                    return False
            start = i2
            while i2 < l2 and abbr[i2].isdigit():
                i2 += 1
            if abbr[start:i2].startswith('0'):
                return False
            i1 += int(abbr[start:i2])
            if i1 == l1 and i2 == l2:
                return True
            if i1 >= l1 or i2 == l2:
                return False


# 比我的解法简洁明了
class Solution1:
    def validWordAbbreviation(self, word: 'str', abbr: 'str') -> 'bool':
        i, n = 0, ''
        for c in abbr:
            if c.isalpha():
                # 前面加0，兼容n为空的情况
                i += int('0' + n)
                if i >= len(word) or c != word[i]:
                    return False
                i, n = i + 1, ''
            else:
                n += c
                # 头字母不能为0
                if n == '0':
                    return False
        return i + int('0' + n) == len(word)
