# Time:  O(n^2)
# Space: O(1)

# 解题思路：
# 考虑用回溯法来解决，此算法的关键点就是[a-z\.]\*可以匹配0-n个字符，无法确定匹配的个数
# 因此只能用回溯递归的方式，只要有一种情况匹配成功，则返回成功，所有的尝试都失败时，返回失败
# 优化思路：当发现pattern中有相同的或者包含关系时(.*和a*)，可以进行合并，需要先进行pattern预处理，否则回溯路径会非常多

import re


class Solution:
    def isMatch(self, s, p):
        pattern = re.compile(r'[a-z.]\*?')
        patterns = re.findall(pattern, p)

        # specific optimization, not scalable, but efficient for this solution
        # pre-process patterns, merge same or including patterns
        def preProcess(patterns):
            # .* merge all adjacent x* pattern
            p_count, p_index = 0, -1
            # count every time after update patterns
            while p_count < patterns.count('.*'):
                index = patterns.index('.*', p_index + 1)
                index_l, index_r = index - 1, index + 1
                while index_l >= 0 and len(patterns[index_l]) == 2:
                    index_l -= 1
                while index_r < len(patterns) and len(patterns[index_r]) == 2:
                    index_r += 1

                patterns = patterns[0:index_l + 1] + patterns[index:index + 1] + patterns[index_r:]
                # update p_index after merge
                p_index = patterns.index('.*', p_index + 1)
                p_count += 1

            # merge a-z* merge all adjacent corresponding a-z and a-z*
            start_index, i, flag, pattern_ch, new_patterns = 0, 0, False, '', []
            for i, pat in enumerate(patterns):
                if pattern_ch != pat or pattern_ch[0] == '.':
                    if flag:
                        new_patterns.append(pattern_ch)
                    else:
                        new_patterns.extend(patterns[start_index:i])

                    flag = len(pat) == 2
                    start_index = i
                    pattern_ch = pat
                elif not flag and len(pat) == 2:
                    flag = True

            if flag:
                new_patterns.append(pattern_ch)
            else:
                new_patterns.extend(patterns[start_index:i + 1])

            return new_patterns

        # match pattern by backtracking
        def isMatchPatterns(s, patterns, index):
            # if patterns has been matched out, check whether reach the end of s
            if len(patterns) == 0:
                return index >= len(s)

            # if there are remain patterns, if all the remains like x*, match success, otherwise failed.
            if index >= len(s):
                return all(len(p) > 1 for p in patterns)

            p = patterns[0]
            if len(p) == 1:
                # when single pattern, if encounter same char or '.', match success, otherwise failed
                if p[0] == s[index] or p[0] == '.':
                    return isMatchPatterns(s, patterns[1:], index + 1)
                else:
                    return False
            elif len(p) == 2:
                # when pattern with *, if encounter same char or '.', match success, otherwise failed
                if p[0] == s[index] or p[0] == '.':
                    # when match success, you can continue to use this pattern, or abandon this and match next pattern.
                    return isMatchPatterns(s, patterns, index + 1) or isMatchPatterns(s, patterns[1:], index)
                # when it failed, match next pattern, not return false, because * can match zero char.
                else:
                    return isMatchPatterns(s, patterns[1:], index)

        return isMatchPatterns(s, preProcess(patterns), 0)


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
class Solution1(object):
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
