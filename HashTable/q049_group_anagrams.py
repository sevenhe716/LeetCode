# Time:  O(n)
# Space: O(1)

# 解题思路：
# 一种思路是利用位置无关的特性，如sum，利用hash做初选，然后再用Counter再次分类
# 另一种思路则是利用hash一步到位，但是需要5*26个bit的大整型，且每个字母个数不能大于32个
# 优化思路：其实无需生成hash，字符串本身可以作为key，利用map来分组


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        import itertools
        from operator import itemgetter

        hashs = [0] * len(strs)
        lst = []

        for i, s in enumerate(strs):
            for c in s:
                hashs[i] += 1 << (ord(c) - ord('a')) * 5

            lst.append({'hash': hashs[i], 'value': s})

        lst.sort(key=itemgetter('hash'))
        # lst.sort(lambda x : x['hash'])
        lstg = itertools.groupby(lst, itemgetter('hash'))

        ans = []
        for key, group in lstg:
            ans.append([g['value'] for g in group])

        return ans


class Solution1(object):
    # Categorize by Sorted String
    def groupAnagrams1(self, strs):
        import collections

        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    # Categorize by Count
    def groupAnagrams(self, strs):
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


class SolutionF:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in d:
                d[ss] = [s]
            else:
                d[ss].append(s)
        ans = []
        for key in d:
            ans.append(d[key])
        return ans
