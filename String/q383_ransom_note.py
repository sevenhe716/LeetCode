# Time:  O(n)
# Space: O(1)

# 解题思路：
# 我们可以假设这个场景是，ransomNote是短字符串，magazine是长字符串
# 首先用两个计数器是消耗比较大的，因此可以考虑只做短字符串的Counter，然后用count进行比较
# 然后可以考虑set去重后，直接用count进行比较
# 效率最高的方式是记录索引位置的find查找法，但这种方法在用例前面填充很多垃圾字符的情况下效率会非常低
from collections import Counter


class Solution(object):
    def canConstruct1(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt1, cnt2 = Counter(ransomNote), Counter(magazine)
        for letter, v in cnt1.items():
            if v > cnt2.get(letter, 0):
                return False
        return True

    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt = Counter(ransomNote)
        for letter, v in cnt.items():
            # if letter not in magazine or v > magazine.count(letter):
            if v > magazine.count(letter):
                return False
        return True

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        pos = {}
        for c in ransomNote:
            if c in pos:
                new_pos = magazine.find(c, pos[c]+1)
            else:
                new_pos = magazine.find(c)

            if new_pos == -1:
                return False
            pos[c] = new_pos
        return True

class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)