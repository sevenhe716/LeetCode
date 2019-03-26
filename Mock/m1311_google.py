# Time:  O(n)
# Space: O(n)

# Ideas:
# satisfy symmetric but not transitive
from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        if len(words1) != len(words2):
            return False
        # one-direction is enough
        similar_dict = defaultdict(list)
        for w1, w2 in pairs:
            similar_dict[w1].append(w2)
        return all(w1 == w2 or w2 in similar_dict[w1] or w1 in similar_dict[w2] for w1, w2 in zip(words1, words2))
