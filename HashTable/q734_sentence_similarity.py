# Time:  O(n)
# Space: O(n)

# 解题思路：
# 建立相似词的单向映射，然后进行单向映射，并判断二者相等，但这个解法是错误的，题目定义相似不具有传递性，而且对原数据具有破坏性
# 依然建立单向索引，当判断二者是否相等，如果不相等，则在字典中进行双向查找（正向匹配或反向匹配）
# 注意有多重映射的情况，这里需要用list，依然单向映射就可以完成
# 优化：实际上使用set即可，存储tuple，还避免了dict(list)的复杂结构
from collections import defaultdict


class Solution:
    def areSentencesSimilar1(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        if len(words1) != len(words2):
            return False

        similar_dict = defaultdict(list)
        for p in pairs:
            similar_dict[p[0]].append(p[1])

        return all(w1 == w2 or w2 in similar_dict[w1] or w1 in similar_dict[w2] for w1, w2 in zip(words1, words2))

    def areSentencesSimilar(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        if len(words1) != len(words2):
            return False

        similar_set = {(p[0], p[1]) for p in pairs}
        return all(w1 == w2 or (w1, w2) in similar_set or (w2, w1) in similar_set for w1, w2 in zip(words1, words2))


class Solution1:
    # 另一种思路，直接用in在list中查找，但效率不一定高
    def areSentencesSimilar(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> 'bool':
        if len(words1) != len(words2):
            return False
        if words1 == words2:
            return True

        for i in range(len(words1)):
            if words1[i] != words2[i] and [words1[i], words2[i]] not in pairs and [words2[i], words1[i]] not in pairs:
                return False

        return True