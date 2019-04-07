# Time:  O(n*4^n)
# Space: O(n)

# 解题思路：
# 递归或循环即可，循环从速度上讲应该快一些


class Solution:
    digit_letters = {0: [], 1: [], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
                     6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}      # list即可

    # recursion
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':            # not digits or len(digits)
            return []

        letters = []

        def combination(index, letter):
            if index >= len(digits):
                letters.append(''.join(letter))
                return

            for l in Solution.digit_letters[int(digits[index])]:
                letter.append(l)
                combination(index + 1, letter)
                letter.pop()

        combination(0, [])

        return letters

    # iterative: 循环的解法，倒序遍历，pop当前元素并扩充成新的元素集合，缺点是顺序会颠倒，前向加就可以解决这个问题
    def letterCombinations1(self, digits):
        if digits == '':
            return []

        letters = [""]

        for i, d in enumerate(digits):
            for j in range(len(letters))[::-1]:     # 倒序遍历, reversed
                letter = letters.pop(j)

                for l in Solution.digit_letters[int(d)]:
                    letters.append(letter + l)      # list拼接应该比字符串更快

        return [''.join(letter) for letter in letters]


# Iterative Solution
class Solution1:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []

        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno",    # list即可，无需dict
                          "pqrs", "tuv", "wxyz"], [""]

        for digit in reversed(digits):
            choices = lookup[int(digit)]
            m, n = len(choices), len(result)
            result += [result[i % n] for i in range(n, m * n)]      # m倍扩充result

            for i in range(m * n):
                result[i] = choices[i / n] + result[i]

        return result


# Time:  O(n * 4^n)
# Space: O(n)
# Recursive Solution
class Solution2:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno",
                          "pqrs", "tuv", "wxyz"], []
        self.letterCombinationsRecu(result, digits, lookup, "", 0)
        return result

    def letterCombinationsRecu(self, result, digits, lookup, cur, n):
        if n == len(digits):
            result.append(cur)
        else:
            for choice in lookup[int(digits[n])]:
                self.letterCombinationsRecu(result, digits, lookup, cur + choice, n + 1)    # 递归若用str则无需push pop


class SolutionF:
    def __init__(self):         # 初始化函数中定义
        self.dt = {'1': '',
                   '2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz',
                   '0': ''}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return [s for s in self.dt[digits[0]]]

        elif len(digits) == 2:                  # 特殊值单独讨论，提高运行速度
            return [a + b for a in self.dt[digits[0]] for b in self.dt[digits[1]]]

        else:
            str_list = self.letterCombinations(digits[1:])  # 基于原函数的递归
            return [a + b for a in self.dt[digits[0]] for b in str_list]    # 简洁




