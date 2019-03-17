# Time:  O(n)
# Space: O(1)

# Ideas:
# hash?
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        res = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            # fingerprint
            res[''.join(str(chr(c)) for c in counter)].append(s)
        return [v for v in res.values()]
