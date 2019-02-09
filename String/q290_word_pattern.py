# Time:  O(n)
# Space: O(1)

# 解题思路：
# 要求一一映射，可以用字典判断key和value是否有重复


class Solution:
    def wordPattern(self, pattern: 'str', str: 'str') -> 'bool':
        words = str.split(' ')
        pattern_word = {}
        if len(pattern) != len(words):
            return False
        for i, p in enumerate(pattern):
            if p in pattern_word:
                if pattern_word[p] != words[i]:
                    return False
            else:
                if words[i] in pattern_word.values():
                    return False
                else:
                    pattern_word[p] = words[i]
        return True


# pythonic的写法
class Solution1:
    # 非常精炼优美的写法，用map返回第一个索引
    def wordPattern1(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))

    # 集合的长度，zip打包后集合的长度
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        if len(s) != len(t):
            return False
        else:
            return len(set(zip(s, t))) == len(set(s)) == len(set(t))