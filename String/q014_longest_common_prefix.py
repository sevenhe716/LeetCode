# Time:  O(m*n)
# Space: O(1)

# 解题思路：
# 一个显而易见的解法就是所有字符串同时遍历即可，时间复杂度为O(m*n)


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""

        if not strs:       # len(strs) < 1
            return prefix

        for i in range(len(strs[0])):
            common = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or common != s[i]:
                    return prefix
            prefix += common

        return prefix


    def longestCommonPrefix2(self, strs):
        res = ''
        # base case 1
        if len(strs) < 1: return res
        size = min(len(s) for s in strs)
        # base case 2 one of them is empty
        if size < 1: return res

        # iteration case
        for i in range(size):
            if all(str1[i] == str2[i] for str1, str2 in zip(strs[:-1], strs[1:])):
                # if strs[0][i] == strs[1][i] == str[2][i]:
                res += strs[0][i]
            else:
                break

        return res


# 无需构建新的字符串，直接在原有字符串上slice前缀即可
class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


class SolutionF:
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)       # 感觉排序的意义并不大，只要长度不满足就终止，每次比较的开销应该比排序小吧
        for i, ch in enumerate(shortest):
            for others in strs:
                if others[i] != ch:
                    return shortest[:i]
        return shortest

    # zip
    def longestCommonPrefix2(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]

        return min(strs)

    # reduce
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        from functools import reduce

        def matching(str1, str2):
            j = 0
            a = min(len(str1), len(str2))
            for i in range(a):
                if str1[i] == str2[i]:
                    j += 1
                else:
                    break
            return str1[:j]

        if len(strs) == 0:
            return ''
        else:
            return reduce(matching, strs)

