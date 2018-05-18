# Time:  O(n)
# Space: O(1)

# 解题思路：
# 创建索引到source target的dict，排序后反向遍历数组并且进行替换
# 注意：index并不一定是有序的，source target中可能有重复的元素

class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        from itertools import count

        s_list = list(S)

        # 不能这样排序，因为sources和targets可能有重复的情况
        # src_index_dict = {sources[i]: k for i, k in enumerate(indexes)}
        # tar_index_dict = {targets[i]: k for i, k in enumerate(indexes)}

        # sources = sorted(sources, key=lambda x: src_index_dict[x])
        # targets = sorted(targets, key=lambda x: tar_index_dict[x])

        src_dict = {k: list(sources[i]) for i, k in enumerate(indexes)}
        tar_dict = {k: list(targets[i]) for i, k in enumerate(indexes)}

        indexes.sort()

        # src_list = [list(s) for s in sources]
        # tar_list = [list(t) for t in targets]

        for i in range(len(indexes))[::-1]:
            start = indexes[i]
            end = start + len(src_dict[start])
            if s_list[start:end] == src_dict[start]:
                s_list = s_list[:start] + tar_dict[start] + s_list[end:]

        return ''.join(s_list)


class SolutionF(object):
    def findReplaceString(self, S, indexes, sources, targets):
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse=True):
            if all(i + k < len(S) and S[i + k] == x[k] for k in range(len(x))):
                S[i:i + len(x)] = list(y)

        return "".join(S)

    def findReplaceStringOneLine(self, S, indexes, sources, targets):
        from functools import reduce

        # tp = (i, s, t)
        return reduce(lambda S, tp: S[:tp[0]] + tp[2] + S[tp[0] + len(tp[1]):] if S[tp[0]:tp[0] + len(tp[1])] == tp[1] else S,
                      sorted(zip(indexes, sources, targets), reverse=True), S)


# To some string S, we will perform some replacement operations that replace groups of letters with new ones (not
# necessarily the same size).
#
# Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is
# that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not,
#  we do nothing.
#
# For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then because
#  "cd" starts at position 2 in the original string S, we will replace it with "ffff".
#
# Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee",
# as well as another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in
#  the original string S[2] = 'c', which doesn't match x[0] = 'e'.
#
# All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: for
# example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.
