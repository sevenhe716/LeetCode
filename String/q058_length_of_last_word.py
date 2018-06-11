# Time:  O(n)
# Space: O(1)

# 解题思路：
# 从后往前找，找到第一个非空格作为end=i+1位置，找到第下一个空格或者直到开头作为start=i+1位置


class Solution:
    def lengthOfLastWord1(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1
        end = i + 1

        while i >= 0 and s[i] != ' ':
            i -= 1
        start = i + 1

        return end - start


class SolutionF:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = s.split()
        return len(x[-1]) if len(x) > 0 else 0