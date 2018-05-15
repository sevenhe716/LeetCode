# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 考虑用回溯法来解决，此算法的关键点就是[a-z\.]\*可以匹配0-n个字符，无法确定匹配的个数
# 因此只能用回溯递归的方式，只要有一种情况匹配成功，则返回成功，所有的尝试都失败时，返回失败
# 优化思路：当发现pattern中有相同的或者包含关系时(.*和a*)，可以进行合并，需要先进行pattern预处理，否则回溯路径会非常多

import re


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        pattern = re.compile(r'[a-z\.]\*?')
        patterns = re.findall(pattern, p)

        patterns = Solution.preProcess(patterns)

        return Solution.isMatchPatterns(s, patterns, 0)

    @staticmethod
    def preProcess(patterns):
        # patterns预处理，合并相同或者包含的模式
        # .*合并所有相邻的x*
        # a-z*合并所有相邻的a-z及a-z*
        p_count = 0
        p_index = -1
        while p_count < patterns.count('.*'):
            index = patterns.index('.*', p_index + 1)
            index_l = index - 1
            index_r = index + 1
            while index_l >= 0 and len(patterns[index_l]) == 2:
                index_l -= 1
            while index_r < len(patterns) and len(patterns[index_r]) == 2:
                index_r += 1

            patterns = patterns[0:index_l + 1] + patterns[index:index + 1] + patterns[index_r:]

            # 移除之后再更新p_index
            p_index = patterns.index('.*', p_index + 1)
            p_count += 1

        flag = False
        pattern_ch = ' '
        start_index = 0
        new_patterns = []

        i = 0

        for i, pat in enumerate(patterns):
            if pattern_ch != pat or pattern_ch[0] == '.':
                if flag:
                    new_patterns.append(pattern_ch)
                else:
                    new_patterns.extend(patterns[start_index:i])

                if len(pat) == 2:
                    flag = True
                else:
                    flag = False

                start_index = i
                pattern_ch = pat
            else:
                if not flag:
                    if len(pat) == 2:
                        flag = True

        if flag:
            new_patterns.append(pattern_ch)
        else:
            new_patterns.extend(patterns[start_index:i + 1])

        return new_patterns

    @staticmethod
    def isMatchPatterns(s, patterns, index):
        # 如果Pattern已经匹配完成，判断是否已经抵达终点
        if len(patterns) == 0:
            if index < len(s):
                return False
            else:
                return True

        # 如果还有剩余的模式没有匹配，如果剩余都是带*，则应该匹配成功，否则匹配失败
        if index >= len(s):
            for p in patterns:
                if len(p) == 1:
                    return False
            return True

        p = patterns[0]

        assert 0 < len(p) <= 2

        if len(p) == 1:
            if p[0] == s[index] or p[0] == '.':
                return Solution.isMatchPatterns(s, patterns[1:], index + 1)
            else:
                return False
        elif len(p) == 2:
            if p[0] == s[index] or p[0] == '.':
                # 如果匹配成功则有两种情况，接着用这个模式匹配下一个，或者抛弃这个模式，用下个模式云匹配
                return Solution.isMatchPatterns(s, patterns, index + 1) \
                       or Solution.isMatchPatterns(s, patterns[1:], index)
            else:
                return Solution.isMatchPatterns(s, patterns[1:], index)
        else:
            return False


# dp with rolling window
class Solution1:
    # @return a boolean
    def isMatch(self, s, p):
        k = 3
        result = [[False for j in range(len(p) + 1)] for i in range(k)]

        result[0][0] = True
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                result[0][i] = result[0][i - 2]

        for i in range(1, len(s) + 1):
            if i > 1:
                result[0][0] = False
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*':
                    result[i % k][j] = result[(i - 1) % k][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    result[i % k][j] = result[i % k][j - 2] or (
                                result[(i - 1) % k][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return result[len(s) % k][len(p)]


# dp
# Time:  O(m * n)
# Space: O(m * n)
class Solution2:
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]

        result[0][0] = True
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                result[0][i] = result[0][i - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*':
                    result[i][j] = result[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    result[i][j] = result[i][j - 2] or (result[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return result[len(s)][len(p)]


# iteration
class Solution3:
    # @return a boolean
    def isMatch(self, s, p):
        p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        last_ptr = []
        while s_ptr < len(s):
            if p_ptr < len(p) and (p_ptr == len(p) - 1 or p[p_ptr + 1] != '*') and \
                    (s_ptr < len(s) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '.')):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) - 1 and (p_ptr != len(p) - 1 and p[p_ptr + 1] == '*'):
                p_ptr += 2
                last_ptr.append([s_ptr, p_ptr])
            elif last_ptr:
                [last_s_ptr, last_p_ptr] = last_ptr.pop()
                while last_ptr and p[last_p_ptr - 2] != s[last_s_ptr] and p[last_p_ptr - 2] != '.':
                    [last_s_ptr, last_p_ptr] = last_ptr.pop()

                if p[last_p_ptr - 2] == s[last_s_ptr] or p[last_p_ptr - 2] == '.':
                    last_s_ptr += 1
                    s_ptr = last_s_ptr
                    p_ptr = last_p_ptr
                    last_ptr.append([s_ptr, p_ptr])
                else:
                    return False
            else:
                return False

        while p_ptr < len(p) - 1 and p[p_ptr] == '.' and p[p_ptr + 1] == '*':
            p_ptr += 2

        return p_ptr == len(p)


# recursive
class Solution4:
    # @return a boolean
    def isMatch(self, s, p):
        if not p:
            return not s

        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])


# Recursion
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


class SolutionF(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
