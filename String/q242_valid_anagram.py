# Time:  O(n)
# Space: O(1)

# 解题思路：
# 一个思路是统计26个字母出现的次数，并进行比较
# 另一个思路是排序后比较字符串
# 优化思路：使用系统库永远是最快的，除非你用的是基本运算
import string
import collections


class Solution:
    # 排序
    def isAnagram1(self, s: 'str', t: 'str') -> 'bool':
        # 是否用这个预检测加速，取决于测试用例的分布特性
        # if len(s) != len(t):
        #     return False
        return sorted(s) == sorted(t)

    # 统计字母数
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        # 原本以为使用定长数组来取代Counter，空间和时间复杂度都会变低，没想到时间复杂度更高
        # 应该是最后一步比较的时候，如果计数器是稀疏的，则比较效率不如dict
        char_counter1, char_counter2 = [0] * 26, [0] * 26
        for c in s:
            char_counter1[ord(c) - ord('a')] += 1
        for c in t:
            char_counter2[ord(c) - ord('a')] += 1
        return char_counter1 == char_counter2


class Solution1:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        for i in string.ascii_lowercase:
            if s.count(i) != t.count(i):
                return False
        return True


class Solution2:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        cnt1 = collections.Counter(s)
        cnt2 = collections.Counter(t)
        if cnt1 == cnt2:
            return True
        else:
            return False
