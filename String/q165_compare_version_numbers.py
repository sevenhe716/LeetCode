# Time:  O(n)
# Space: O(1)

# Ideas:
# split, convert to number and compare
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        if len(v1) < len(v2):
            v1 += [0] * (len(v2) - len(v1))
        else:
            v2 += [0] * (len(v1) - len(v2))
        if v1 == v2:
            return 0
        if v1 < v2:
            return -1
        else:
            return 1


class Solution1:
    # string -> int compare
    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':
        first = version1.split('.')
        second = version2.split('.')
        while len(first) < len(second):
            first.append("0")
        while len(second) < len(first):
            second.append("0")

        for a, b in zip(first, second):
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
        if len(first) > len(second):
            return 1
        elif len(first) < len(second):
            return -1
        else:
            return 0

    # Pad with izip_longest with fillvalue=0
    def compareVersion1(self, version1, version2):
        v1, v2 = map(int, version1.split('.')), map(int, version2.split('.'))
        v1, v2 = zip(*zip_longest(v1, v2, fillvalue = 0))
        return (v1 > v2) - (v1 < v2)
        # return cmp(*zip(*itertools.izip_longest(*splits, fillvalue=0)))

    # Pad with [0] * lengthDifference
    def compareVersion2(self, version1, version2):
        v1, v2 = map(int, version1.split('.')), map(int, version2.split('.'))
        d = len(v2) - len(v1)
        v1, v2 = v1 + [0] * d, v2 + [0] * -d
        return (v1 > v2) - (v1 < v2)

    # Recursive, add zeros on the fly
    def compareVersion3(self, version1, version2):
        main1, _, rest1 = ('0' + version1).partition('.')
        main2, _, rest2 = ('0' + version2).partition('.')
        return (int(main1) > int(main2)) - (int(main1) < int(main2)) or \
               len(rest1 + rest2) and self.compareVersion(rest1, rest2)