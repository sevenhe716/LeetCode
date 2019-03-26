# Time:  O(n)
# Space: O(1)

# Ideas:
# same length and same diff, use group or dict
from itertools import groupby
from collections import defaultdict
import string


class Solution:
    # group by
    def groupStrings1(self, strings: 'List[str]') -> 'List[List[str]]':
        def lambda_shift(x):
            return [(ord(c) - ord(x[0])) % 26 for c in x]

        # grouby需要先排序
        shift_group = groupby(sorted(strings, key=lambda_shift), key=lambda_shift)
        return [list(j) for _, j in shift_group]

    # dict
    def groupStrings(self, strings: 'List[str]') -> 'List[List[str]]':
        str_dict = defaultdict(list)
        for s in strings:
            str_dict[tuple((ord(c) - ord(s[0])) % 26 for c in s)].append(s)
        return [*str_dict.values()]


class Solution1:
    def groupStrings(self, strings: 'List[str]') -> 'List[List[str]]':
        lexicon = {}
        hashmap = defaultdict(list)

        # 索引加速查询
        for i, l in enumerate(string.ascii_lowercase):
            lexicon[l] = i

        for word in strings:
            datum = word[0]
            datum_pos = lexicon.get(datum)
            key = tuple()

            for i, letter in enumerate(word):
                offset = lexicon.get(letter) - datum_pos
                if offset < 0:
                    offset += 26
                key += (offset,)

            hashmap[key].append(word)

        return [*hashmap.values()]