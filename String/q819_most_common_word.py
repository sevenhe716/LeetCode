# Time:  O(n)
# Space: O(1)

# Ideas:
# mark
import re
from collections import Counter
from operator import itemgetter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: 'List[str]') -> str:
        ban = set(banned)
        words = list(filter(None, re.split('[^a-zA-Z]', paragraph.lower())))
        counter = Counter(filter(lambda x: x not in ban, words))
        return max(counter.items(), key=itemgetter(1))[0]


class Solution1:
    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        # most_common
        return Counter(w for w in words if w not in ban).most_common(1)[0][0]