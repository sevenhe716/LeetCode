# Time:  O(nlogn)
# Space: O(1)

# Ideas:
# same length and same diff, use group or dict
from itertools import groupby


class Solution:
    # group by
    def groupStrings(self, strings: 'List[str]') -> 'List[List[str]]':
        res = []
        strings.sort(key=len)
        len_group = groupby(strings, key=len)

        def lambda_shift(x):
            return [(ord(c) - ord(x[0])) % 26 for c in x]

        for _, len_grp in len_group:
            shift_group = groupby(sorted(len_grp, key=lambda_shift), key=lambda_shift)

            for i, j in shift_group:
                res.append([g for g in j])
        return res
