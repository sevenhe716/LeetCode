# Time:  O(m+n)
# Space: O(1)

# 解题思路：
# KMP算法

class Solution:
    def strStr(self, haystack, needle):
        # Return 0 if needle is ""
        if not needle:
            return 0
        length = len(haystack)

        # If one char in haystack is same with needle[0],
        # then verify the other chars in needle.
        for i in range(length-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
            # create kmp table
        table = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j != 0 and needle[i] != needle[j]:
                j = table[j - 1]
            if needle[i] == needle[j]:
                j += 1
                table[i] = j
        j = 0
        # search the needle
        for i in range(len(haystack)):
            while j != 0 and haystack[i] != needle[j]:
                j = table[j - 1]
            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle):
                    return i - j + 1
        # not found return -1
        return -1