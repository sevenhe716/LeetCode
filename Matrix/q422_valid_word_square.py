# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 注意每行每列并不一定是等长的
# 一个想法是用一个二维矩阵来存储，没有值的地方填非alphabet的字符即可，然后判断值是否相等，比较直观，代码逻辑简单，但有O(n^2)的空间复杂度
# 另一个解法就是直接在list[str]的基础上比较，空间复杂度更低，为O(1)
from itertools import zip_longest


class Solution:
    # 空间复杂度O(n^2)
    def validWordSquare1(self, words: 'List[str]') -> bool:
        max_len = len(max(words, key=len))
        if max_len != len(words):
            return False
        matrix = [['*'] * max_len for _ in range(max_len)]
        for i, word in enumerate(words):
            matrix[i][:len(word)] = list(word)
        return all(matrix[i][j] == matrix[j][i] for i in range(max_len) for j in range(max_len))

    # 空间复杂度O(1)
    def validWordSquare(self, words: 'List[str]') -> bool:
        max_len = len(max(words, key=len))
        if max_len != len(words):
            return False
        return not any(j >= len(words[i]) and i < len(words[j])
                       or j < len(words[i]) and i >= len(words[j])
                       or j < len(words[i]) and i < len(words[j]) and words[i][j] != words[j][i]
                       for i in range(max_len) for j in range(max_len))
        # for i in range(max_len):
        #     for j in range(max_len):
        #         if j >= len(words[i]) and i < len(words[j]) or j < len(words[i]) and i >= len(words[j]):
        #             return False
        #         if j < len(words[i]) and i < len(words[j]) and words[i][j] != words[j][i]:
        #             return False
        # return True


class Solution1:
    # The map(None, ...) transposes the "matrix", filling missing spots with None
    def validWordSquare1(self, words):
        return map(None, *words) == map(None, *map(None, *words))

    def validWordSquare2(self, words):
        f = lambda x: map(None, *x)  # padded Transpose
        return f(f(words)) == f(words)

    def validWordSquare3(self, words: 'List[str]') -> 'bool':
        for i, tup in enumerate(zip_longest(*words, fillvalue='')):
            if ''.join(tup) != words[i]:
                return False
        return True

    def validWordSquare4(self, words):
        return map("".join, zip_longest(*words, fillvalue='')) == words

    def validWordSquare5(self, words):
        other = list(zip_longest(*words))
        return not any(i >= len(other) or j >= len(other[i]) or other[i][j] != char
                       for i, word in enumerate(words)
                       for j, char in enumerate(word))
