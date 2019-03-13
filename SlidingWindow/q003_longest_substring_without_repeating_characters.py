# Time:  O(n)
# Space: O(n)

# 解题思路：
# 顺序遍历，当出现重复时记录当前的长度，并与历史最大长度比较，继续遍历直到结束
# 用list来存储最大子串（因为string是不可变的），当检测到重复时，从该位置左截断继续遍历
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """

        sub_str = []
        max_len = 0

        for i in range(len(s)):
            if s[i] in sub_str:
                max_len = max(max_len, len(sub_str))
                sub_str = sub_str[sub_str.index(s[i]) + 1:]

            sub_str.append(s[i])

        max_len = max(max_len, len(sub_str))
        return max_len

    # 本想过用256位的hashtable元组来存储，但感觉丢失了序列索引的信息，所以放弃了这种思路，其实可以维护一个起始指针就可以实现了
    # 空间复杂度降为O(1)
    def lengthOfLongestSubstring2(self, s):
        longest, start, visited = 0, 0, [False] * 256
        for i, c in enumerate(s):
            if visited[ord(c)]:
                while c != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(c)] = True
            longest = max(longest, i - start + 1)
        return longest

    # substring template
    def lengthOfLongestSubstring(self, s):
        counter = defaultdict(int)
        count, start, end, res = 0, 0, 0, 0
        while end < len(s):
            if counter[s[end]] > 0:
                count += 1
            counter[s[end]] += 1
            end += 1
            while count > 0:
                if counter[s[start]] > 1:
                    count -= 1
                counter[s[start]] -= 1
                start += 1
            res = max(res, end - start)
        return res


# 跟上面的思路类似，但是把存bool转化为了存索引值，比较索引值即可
class SolutionF:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hash_table = {}
        max_len = 0
        cur = 0

        for i, c in enumerate(s):
            if c in hash_table and cur <= hash_table[c]:
                cur = hash_table[c] + 1
            else:
                max_len = max(max_len, i - cur + 1)
            hash_table[c] = i

        return max_len

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        L, res, last = -1, 0, {}
        for R, char in enumerate(s):
            if char in last and last[char] > L:
                L = last[char]
            elif R - L > res:
                res = R - L
            last[char] = R
        return res

# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
#
# "pwke" is a subsequence and not a substring.
