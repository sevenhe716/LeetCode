# Time:  O(n)
# Space: O(1)

# Ideas:
# mark
import re
from collections import Counter
from operator import itemgetter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: 'List[str]') -> str:
        words = list(filter(None, re.split('[^a-zA-Z]', paragraph.lower())))
        # paragraph = ''.join([c for c in paragraph if c.isalpha() or c.isspace()])
        # paragraph = ''.join(filter(str.isalpha or str.isspace, paragraph))
        # words = paragraph.split()
        counter = Counter(filter(lambda x: x not in banned, words))
        return max(counter.items(), key=itemgetter(1))[0]