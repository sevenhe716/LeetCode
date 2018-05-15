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

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.
